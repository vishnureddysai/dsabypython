import datetime as dt

print("hey! welcome to vishnu hotel")
name = input("can i know ur name please?...\n")
print("once again welcome mr/mrs/miss {}".format(name))
print("im ur assistance")
sno=[1,2,3]
facility = []
pr = []
be = '''
1.wifi
2.food
'''
h_p = {"single_room":400,"doubleroom":600}
f_p = {"food":300,"wifi":75}
t = int(input("would u like know to our hotel facility choose 1 and 2 for our room and facility prices "))
if t==1:
    print(be)
else:
    a = str(h_p)
    b = a.replace("}","")
    c = b.replace("{","")
    d = c.replace(",","")
    
    print("room prices are \n",d)
    print("facility prices are \n",f_p)
k = int(input("would like to book a room \n if yes enter 1 and no for 2\n"))
if k==1:
    ty = input("enter the room type you want \n")
    amount = 0
    for i in h_p.keys():
        if i==ty:
            t1 = h_p[i]
            amount += t1
            pr.append(t1)
            facility.append(ty)
            fac = input("along with {} would you like any benefit wifi or food\n".format(ty))
            facility.append(fac)
            for j in f_p.keys():
                if j==fac:
                    t2 = f_p[j]
                    pr.append(t2)
                    amount += t2
    #print(amount)
    print("-"*20,"vishnu's hotel","-"*20)
    print("name :",name)
    x = dt.datetime.now()
#print(x.year)
    print("date:",x.strftime("%d-%b-%Y"))
    print("day:",x.strftime("%A"))
    print("time:",x.strftime("%H:%M:%S"))

    print("s.no\t\t\tfacility\t\tprice")
    for l in range(0,2):
        print(sno[l],"|\t\t\t",facility[l],"|\t\t\t",pr[l],"|")
    print("\t\t\t\t\t\t\t",amount)
    print("please visit us again... thank you {}".format(name))

else:
    print("please visit us next time if u would like thank you {}".format(name))
