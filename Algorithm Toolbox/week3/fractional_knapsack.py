def get_optimal_value(n,capacity, weights, values):
    value = 0
    values,weights=(list(t) for t in zip(*sorted(zip(values,weights),key=lambda x:-x[0]/x[1])))
    for i in range(n):
        if capacity==0:
            break
        r=min(capacity,weights[i])
        value+=r*(values[i]/weights[i])
        capacity-=r
    return value

n, capacity = map(int, input().split())
values=[0]*n
weights=[0]*n
for i in range(n):
    values[i],weights[i]= map(int, input().split())
opt_value = get_optimal_value(n,capacity, weights, values)
print("{:.4f}".format(opt_value))
