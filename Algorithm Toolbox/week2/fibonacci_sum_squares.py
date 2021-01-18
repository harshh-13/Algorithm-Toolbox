n = int(input())
l=[0]*30
r=[0]*30
l[0]=0
l[1]=1
for i in range(2,30):
    l[i]=l[i-1]+l[i-2]
for i in range(30):
    l[i]=l[i]**2%10
    r[i]=sum(l[:i+1])%10
print(r[n%30])
