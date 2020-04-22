f= open('wde.txt' ,'r')
for kh in f:
  kh=kh.rstrip()
  kh=kh.replace(" ",".")
  print(kh ,'888')
  kh=kh+"@ya.com"
  print(kh)
