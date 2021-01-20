def solution(X, A):
    pos = set()
    for i,j in enumerate(A):
        pos.add(j)
        if len(pos) == X:
            return i
        print(pos)
    return -1


print(solution(5,[1,3,1,4,2,3,5,4]))