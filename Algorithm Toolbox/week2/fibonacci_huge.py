def fibonacci_huge(h,n):
    if n<=1:
        return 0
    s=[]
    a=0;k=0;b=1
    while s[:k]!=s[k:] or k<1:
        s.append(a%n)
        k=len(s)//2
        a,b=b,a+b
    return s[h%k]

n, m = map(int, input().split())
print(fibonacci_huge(n, m))
