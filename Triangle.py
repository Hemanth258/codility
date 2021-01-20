def solution(A):
    A.sort()
    f = []
    for i in range(len(A)-2):
        if A[i]+A[i+1]>A[i+2]:
            f.append(1)
        else:
            f.append(0)
    if 1 in f:
        return 1
    else:
        return 0
print(solution([10,2,5,1,8,20]))