def solution(A):
	c = 0
	arr = []
	for i in A:
		c+=1
		if sum(A[:c])>sum(A[c:]):
			arr.append(sum(A[:c])-sum(A[c:]))
		else:
			arr.append(sum(A[c:])-sum(A[:c]))
	arr.pop()
	return min(arr)
print(solution([3,1,2,4,3]))