def filtra_pares(A):
    B=A
    if B[0]/2==B[0]//2:
         A=B[0]
    if B[1]/2==B[1]//2:
        A=A+B[1]
    if B[2]/2==B[2]//2:
        A=A+B[2]
    if B[3]/2==B[3]//2:
        A=A+B[3]
    return A