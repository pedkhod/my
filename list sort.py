a=int(input("enter a number"))
my_list=[]
try:
 while True:
   my_list.append(a)
   a=int(input("enter a number"))
except:
 for i in range(0,len(my_list)):
    for j in range(0,i):
        if my_list[i]>my_list[j]:
            a=my_list[j]
            my_list[j]=my_list[i]
            my_list[i]=a
print(my_list)
