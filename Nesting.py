def solution(S):
	try:
		arr = []
		for i in S:
			if i == '(':
				arr.append(i)
			if i == ')':
				arr.pop()
		if len(arr)==0:
			return 1
		else:
			return 0
	except Exception as e:
		return 0
print(solution( "(()(())())"))