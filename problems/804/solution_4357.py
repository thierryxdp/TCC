def filtra_pares(A):
    if not A[0]/2==A[0]//2:
        A=A[-0]
    if not A[1]/2==A[1]//2:
        A=A[-1]
    if not A[2]/2==A[2]//2:
        A=A[-2]
    if not A[3]/2==A[3]//2:
        A=A[-3]
    return A