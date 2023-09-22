def busca(s,A):
    l = []
    for i in range(len(A)):
        if A[i][2] == s:
            l += [A[i]]
    return l