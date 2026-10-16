import json

with open("data.json", "r") as file:
    data = json.load(file)


print(type(data))
wos = data['workOrders']#list
print(len(wos))
print(type(wos[0])) #dict for individual wo
for wo in wos:
    print(wo['workorderId'])
