def max_dot_product(a, b):
    a.sort()
    b.sort()
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

n= int(input())
a = list(map(int, input().split()))
b= list(map(int, input().split()))
print(max_dot_product(a, b))
    
