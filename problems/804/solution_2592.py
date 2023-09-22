def filtra_pares(A):
    A=(A[0]%2==0,A[1]%2==0,A[2]%2==0,A[3]%2==0)
    return A[0],A[1],A[2],A[3]