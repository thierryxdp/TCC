def filtra_pares(A):
    B=A
    if A[0]/2==A[0]//2:
         B=(A[0],)
    if A[1]/2==A[1]//2:
        B=(B,)+(A[1],)
    if A[2]/2==A[2]//2:
        B=B,+(A[2],)
    if A[3]/2==A[3]//2:
        B=B,+(A[3])
    return B