def solution(A, K):
	for i in range(K):
		if len(A) != 0:
			p = A.pop()
			A.insert(0,p)
		else:
			pass
	return A

print(solution([1,2,3,5],1))