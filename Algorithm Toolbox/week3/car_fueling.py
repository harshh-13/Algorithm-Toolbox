def compute_min_refills(n, d, m, l):
    r = 0;lst = 0;cur = 0
    l.append(d)
    while cur < len(l):
        if l[cur] - l[lst] <= m:
            cur += 1
        elif l[cur] - l[cur-1] > m or cur == 0:
            return -1
        else:
            lst = cur-1
            r += 1
    return r
d = int(input())
m = int(input())
n = int(input())
stops = list(map(int, input().split()))
print(compute_min_refills(n, d, m, stops))
