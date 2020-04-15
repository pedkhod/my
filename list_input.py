a=int(input("how many item in the list"))
my_list=[]
for d in range(0,a) :
    s=input("enter your next item")
    my_list.append(s)
print(my_list)
z=set(my_list)
my_list=list(z)
print(my_list)
