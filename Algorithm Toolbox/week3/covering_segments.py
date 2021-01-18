n= int(input())
seg=[]
ans = []
for _ in range(n):
    a = list(map(int, input().split()))
    seg.append(a)
if n==1:
    print(1)
    print(seg[0][-1])
else:
    cur = 1
    st = 0
    seg = sorted(seg,key=lambda x:x[1])
    ans.append(seg[st][1])
    while cur < n :
        if seg[st][1]<seg[cur][0]:
            st=cur
            ans.append(seg[st][1])
        cur+=1
    print(len(ans))
    print(*ans)
