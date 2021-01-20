def solution(A):
    m = max(A)
    if m<0:
        return 1
    else:
        e = set([e for e in range(1,m+2)]) - set(A)
        return min(e)