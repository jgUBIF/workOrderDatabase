import requests
import json
import pandas as pd

#for range of all work orders in nextgen, check if it's for uni, and then save the data


# Set up the headers, including auth/cookies
headers = {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json",
    "priority": "u=1, i",
    "x-channel-id": "paste from chrome",
    "x-fs-session": "paste from chrome",
    "x-response-id": "paste from chrome",
    "Referer": "https://portal.ubreakifix.net/repair/workorder/30926049",

    # ⚠️ ADD YOUR AUTHENTICATION HERE:
    "Cookie": "paste from chrome"
}

#open list of all uni closed workorders
with open("data.json", "r") as file:
    data = json.load(file)


print(type(data))
workorders = data['workOrders']#list
print(len(workorders))

#make a list to write data to
dataFrameDict = {
    "workorder": [],
    "event": []
}


for workorder in workorders: #dict for each individual workorder
    workorderId = workorder['workorderId']
    
    #workorder target URL
    url = f"https://portal.ubreakifix.net/api/workorder/{workorderId}/events?pageSize=50"
    print(url)

    response = requests.get(url, headers=headers)

    print(f"Status Code: {response.status_code}")
    try:
        json = response.json()
        print(type(json))
    except ValueError:
        print(response.text)



    for event in json['events']: #each is a 

        dataFrameDict['workorder'].append(workorderId)
        dataFrameDict['event'].append(event['eventData'])
        #print(event['eventData']['items'][0]['itemId'])
        #dataFrameDict['itemId'].append(event['eventData']['items'][0]['itemId'])
        #print(event['eventData']['items'][0])
        #dataFrameDict['event'].append(event['eventData']['items'][0])
        print()


df = pd.DataFrame(dataFrameDict) #making a pandas dataframe
df.to_excel("database.xlsx")

