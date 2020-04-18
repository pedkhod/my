def PerNum(x):
    s=0
    for i in range(1,x):
        if (x % i == 0):
            s=s+i

    if x==s:
        return True
    else:
       return False

mylist=[]
for j in range (1,10000):
    if PerNum(j)==True:
        mylist.append(j)
print(mylist)
