def filtra_pares(tupla):
    """teste"""
    (a,b,c,d) = tupla
    pares = []
    if int(tupla[0]) % 2 == 0:
        pares + tupla[0]
    if int(tupla[1]) % 2 == 0:
        pares + tupla[1]
    if int(tupla[2]) % 2 == 0:
        pares + tupla[2]
    if int(tupla[3]) % 2 == 0:
        pares + tupla[3]
    return pares