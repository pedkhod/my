def PerNum(x):
    s=0
    for i in range(1,x):
        if (x % i == 0):
            s=s+i

    if x==s:
        return True
print(PerNum(28))
