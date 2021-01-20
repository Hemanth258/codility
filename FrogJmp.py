def solution(X,Y,D):
	c = 0
	while X<Y:
		X+=D
		c+=1
	return c
print(solution(10,85,30))