def solution(S, P, Q):
    final = []
    for i in range(len(P)):
        z = (S[P[i]:Q[i]+1])
        if "A" in z:
            final.append(1)
        elif "C" in z:
            final.append(2)
        elif "G" in z:
            final.append(3)
        elif "T" in z:
            final.append(4)
    return final        
print(solution('CAGCCTA',[2,5,0],[4,5,6]))