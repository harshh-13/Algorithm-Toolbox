n = int(input())
l=[0]*60
l[0]=0
l[1]=1
for i in range(2,60):
    l[i]=l[i-1]+l[i-2]
for i in range(2,60):
    l[i]=(l[i]%10+l[i-1]%10)%10
print(l[n%60])
