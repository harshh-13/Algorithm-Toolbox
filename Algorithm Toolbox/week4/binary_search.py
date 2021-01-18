l1=list(map(int, input().split()))
l2=list(map(int, input().split()))
n,k=l1[0],l2[0]
l1=l1[1:]
for i in l2[1:]:
    ind=-1
    h1=0;h2=n-1
    while h1<=h2:
        m=(h1+h2)//2
        if l1[m]==i:
            ind=m
            break
        elif i>l1[m]:
            h1=m+1
        else:
            h2=m-1
    print(ind,end=' ')
