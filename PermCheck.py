def solution(A):
    mi = min(A)
    mx = max(A)
    e = set([e for e in range(mi, mx+1)]) - set(A)
    if len(e) == 0:
        return 1
    else:
        return 0