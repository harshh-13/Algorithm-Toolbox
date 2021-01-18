def get_change(m):
    c=(m//10)+(m%10)//5+(m%5)
    return c
m = int(input())
print(get_change(m))
