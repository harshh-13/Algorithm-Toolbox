def IsGreaterOrEqual(digit, m):
    return int(str(digit)+str(m))>=int(str(m)+str(digit))
n=int(input())
a=list(map(int,input().split()))
ans=[]
while len(a)!=0:
    m=0
    for digit in a:
        if IsGreaterOrEqual(digit, m):
            m=digit
    ans.append(m)
    a.remove(m)
for i in ans:
    print(i,end='')

