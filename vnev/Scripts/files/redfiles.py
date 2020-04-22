f= open('wde.txt' ,'r')
s=open("email.txt","w+")
for kh in f:
  kh=kh.rstrip()
  kh=kh.replace(" ",".")
  print(kh ,'888')
  kh=kh+"@ya.com"
  print(kh)
  s.writelines(kh)
f.close
for s1 in s:
    print(s1)
