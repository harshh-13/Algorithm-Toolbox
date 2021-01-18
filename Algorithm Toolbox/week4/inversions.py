def merge(arr, l, m, r):
	inv=0
	n1 = m - l + 1
	n2 = r- m
	L = [0] * (n1)
	R = [0] * (n2)
	for i in range(n1):
		L[i] = arr[l + i]
	for j in range(n2):
		R[j] = arr[m + 1 + j]
	i,j,k = 0,0,l
	while i < n1 and j < n2 :
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			inv+=n1-i
			arr[k] = R[j]
			j += 1
		k += 1
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1
	return inv
def mergeSort(arr,l,r):
	ans=0
	if l < r:
		m = (l+(r-1))//2
		ans+=mergeSort(arr, l, m)
		ans+=mergeSort(arr, m+1, r)
		ans+=merge(arr, l, m, r)
	return ans
n = int(input())
arr = list(map(int,input().split()))
print(mergeSort(arr,0,n-1))
