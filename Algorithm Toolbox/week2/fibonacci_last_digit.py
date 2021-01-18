n = int(input())
if n<=1:
    print(1)
else:
    l=[0]*(n+60)
    l[0]=0
    l[1]=1
    for i in range(2,60):
        l[i]=(l[i-1]+l[i-2])%10
    if n>60:
        for i in range(61,n+1):
            l[i]=l[i%60]
    print(l[n])

