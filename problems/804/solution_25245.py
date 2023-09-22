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
        A=tupla[0]
    if tupla[1] % 2 == 0:
        B=tupla[1]
    if tupla[2] % 2 == 0:
        C=tupla[2]
    if tupla[3] % 2 == 0:
        D=tupla[3]
    return A+B+C+D