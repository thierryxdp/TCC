def filtra_pares(tup):
    """dado uma tupla com 4 elementos inteiros, a função retorna uma tupla
    com somente os números pares;
    tup->tup"""

    a=tup[0]
    b=tup[1]
    c=tup[2]
    d=tup[3]

    if a%2==0:
        A=(a,)
    else:
        A=()
    if b%2==0:
        B=(b,)
    else:
        B=()
    if c%2==0:
        C=(c,)
    else:
        C=()
    if d%2==0:
        D=(d,)
    else:
        D=()

    return A+B+C+D