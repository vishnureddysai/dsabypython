vo = {'a':0,'e':1,'i':2,'o':2,'u':3}
st = input("enter the key:")
st2 = ""
l = len(st)
for i in vo.keys():
    for j in st:
        if i==j:
            st = st.replace(i,str(vo[i]))
        else:
            pass
for k in range(l-1,-1,-1):
    st2 += st[k]

print('"'+st2+"aca"+'"')
