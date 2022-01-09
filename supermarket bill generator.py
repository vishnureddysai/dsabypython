
name = input("enter customer name ")
address = input("enter address")
phoneno = int(input("enter the phone number of the customer"))
sno = []
values = []
quantity = []
itemadded = []
price = []
items = {'sugar':10,'honey':5,'flour':20,'rava':25,'samiya':30}
n = int(input("please enter the total no of items you need"))
for i in range(0,n):
    t = input("enter the item name")
    q = int(input("enter the quantity"))
    quantity.append(q)
    itemadded.append(t)
    for k in items.keys():
        if t==k:
           val = items[k]
           values.append(val)
for k in range(0,n):
    pri = (values[k] * quantity[k])
    price.append(pri)

for j in range(1,n+1):
    sno.append(j)
for p in price:
    print(p)

print("super market bill generator")
print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
print("\t\t\t\t\t vishnu super market\t\t\t\t\t")
print("name:",name)
print("address:",address)
print("phonemo:",phoneno)

print("sno\t\titemname\t\tquantity\t\tpriceperkg\t\tprice")

for r in range(0,n):
    print(sno[r],"\t\t",itemadded[r],"\t\t\t\t",quantity[r],"\t\t\t",values[r],"\t\t",price[r])
total = 0
for e in price:
    total += e 
print("\t\t\t\t\t\t\t\t\t\t total= ",total)