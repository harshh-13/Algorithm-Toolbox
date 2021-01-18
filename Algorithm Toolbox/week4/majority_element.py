n=int(input())
l=list(map(int, input().split()))
# d={}
# for i in l:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# f=0
# for i in list(d.values()):
#     if i>n//2:
#         print(1)
#         f=-1
#         break
# if f==0:
#     print(0)
c,m=1,l[0]
for i in range(1,n):
    if l[i]==m:
        c+=1
    else:
        c-=1
    if c==0:
        m=l[i]
        c=1
if c>0:
    ct=0
    for i in l:
        if i==m:
            ct+=1
    if ct>n//2:
        print(1)
    else:
        print(0)
else:
    print(0)
