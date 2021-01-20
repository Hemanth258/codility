def solution(A):
    c = -1
    f = 0
    zers = []
    ones = []
    for i in A:
        c+=1
        if i ==0:
            zers.append(c)
        else:
            ones.append(c)
    for z in zers:
        for o in ones:
            if z<o:
                f+=1
    return f
print(solution([0,1,0,1,1]))