def filtra_pares(A):
    a=A[0]%2==0
    b=A[1]%2==0
    c=A[2]%2==0
    d=A[3]%2==0
    return A[0],A[1]%2,A[2]%2,A[3]%2