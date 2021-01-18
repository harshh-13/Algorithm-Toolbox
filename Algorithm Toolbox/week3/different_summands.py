n = int(input())
c=0
l=[]
if n<=2:
    print(1,n,sep='\n')
else:
    for i in range(1,n+1):
        c+=i
        if c==n:
            print(i)
            print(*l,end=' ')
            print(i)
            break
        elif c>n:
            break
        l.append(i)
    if c>n:
        l.pop()
        l.append(n-sum(l))
        print(len(l))
        print(*l)
