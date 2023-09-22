def busca(setor,A):
    for i in range(len(A)):
        if setor in A[i]:
            return A[i]