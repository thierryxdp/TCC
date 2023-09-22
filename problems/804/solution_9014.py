def filtrar_pares(a, b, c, d):
    A = (a, b, c, d,)
    AA = A[0] % 2
    BB = A[1] % 2
    CC = A[2] % 2
    DD = A[3] % 2
    if AA == 0 and BB != 0 and CC != 0 and DD != 0:
        return A[0]
    if AA == 0 and BB == 0 and CC != 0 and DD != 0:
        return A[0:1]
    if AA == 0 and BB == 0 and CC == 0 and DD != 0:
        return A[0:2]
    if AA == 0 and BB == 0 and CC != 0 and DD == 0:
        return A[0:3]