def binary(N):
	conv = bin(N)[2:]
	l = len(conv)
	print(conv)
	check = []
	for i in range(l):
		i = '1'
		check.append(i)
	check = "".join(check)
	if conv == check:
		return 0
	elif(conv != check):
		arr = []
		c = -1
		for i in conv:
			c+=1
			if i == '1':
				arr.append(c)
		res = 0
		fin = []
		for j in arr:
			res = j-res
			fin.append(res)
		if (max(fin)) == 0:
			return 0
		else:
			return (max(fin)-1)
print(binary(1041))
