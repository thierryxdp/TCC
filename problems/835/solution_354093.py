def melhor_volta(A):
    C=[]
    for i in range(len(A)):
        soma = 0
        for j in range(len(A[0])):
            soma = A[i][j]
        list.append(C,soma)
    melhort = min(C)
    return melhort