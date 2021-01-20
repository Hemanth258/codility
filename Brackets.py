def solution(A):
    arr = []
    try:   
        for i in range(len(A)):
            if A[0] == ")" or A[0] == "]" or A[0]=="}":
                return 0
            elif A[i] == ")":
                if arr[len(arr)-1]=="(":
                    arr.pop()
            elif A[i] == "]":
                if arr[len(arr)-1]=="[":
                    arr.pop()
            elif A[i] == "}":
                if arr[len(arr)-1]=="{":
                    arr.pop()
            else:
                arr.append(A[i])
        if len(arr) == 0:
            return 1
        else:
            return 0
    except Exception as e:
        return 0
print(solution("{[()()]}"))