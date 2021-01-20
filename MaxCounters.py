def solution(N, A):
    arr = []
    for i in range(N):
        arr.append(0)
    for i in A:
        m = max(arr)
        if i < N:
            if arr[i-1] == 0:
                arr[i-1] = 1
            else:
                c = arr[i-1]+1
                arr[i-1] = c
        else:
            for i in range(N):
                arr[i] = m
    return arr
print(solution(5,[3,4,4,6,1,4,4]))