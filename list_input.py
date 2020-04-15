a=int(input("how many item in the list"))
my_list=[]
for d in range(0,a) :
    s=input("enter your next item")
    my_list.append(s)
print(my_list)
for i in range(0,len(my_list)):
    s=my_list[i]
    j=i+1
    if j> len(my_list):
       for a in range(j,len(my_list)):
           if my_list[a]==s:
             my_list.pop(a)
print(my_list)
