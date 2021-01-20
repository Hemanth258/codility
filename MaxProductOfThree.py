def solution(A):
    A.sort()
    arr = []
    for i in range(len(A)-2):
        arr.append(A[i]*A[i+1]*A[i+2])
    return max(arr)

print(solution([-3,1,2,-2,5,6]))