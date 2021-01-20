def solution(A):
	for i in A:
		if A.count(i) == 1:
			return int(i)
print(solution([9,3,9,3,7,9]))