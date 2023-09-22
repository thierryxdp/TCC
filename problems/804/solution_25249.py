def filtra_pares(t,):
    tupla=t
    a=tupla[0]
    b=tupla[1]
    c=tupla[2]
    d=tupla[3]
    A=()
    B=()
    C=()
    D=()
    if tupla[0]% 2 == 0:
        A=(a)
    if tupla[1] % 2 == 0:
        B=(b+A)
    if tupla[2] % 2 == 0:
        C=(c+B)
    if tupla[3] % 2 == 0:
        D=(d+C)
    return A+B+C+D