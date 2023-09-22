def soma(numero,A):
    conta=0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j]==numero:
                conta=conta+list.count(A[i][j],numero)
    return conta