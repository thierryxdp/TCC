def filtra_pares(A):
    A=tuple(A)
    C=tuple()
    if A[0]/2==A[0]//2:
        C=(C)+(A[0],)
    if A[1]/2==A[1]//2:
        C=(C)+(A[1],)
    if A[2]/2==A[2]//2:
        C=(C)+(A[2],)
    if A[3]/2==A[3]//2:
        C=(C)+(A[3],)
    return C