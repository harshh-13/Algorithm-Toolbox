m,n=map(int,input().split())
l=[0]*60
l[0]=0
l[1]=1
for i in range(2,60):
    l[i]=l[i-1]+l[i-2]
for i in range(2,60):
    l[i]=l[i]%10
r=sum(l)
if n-m<60:
    print(sum(l[m%60:(n%60)+1])%10)
else:
    c=0
    while m%60!=0:
        c+=l[m%60]
        m+=1
    while n%60!=0:
        c+=l[n%60]
        n-=1
    c+=((n-m)//60)*r
    print(c%10)
