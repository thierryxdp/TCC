def filtra_pares ([a, b ,c ,d]):
    '''recebe uma tupla com quatro elementos inteiros e retorna apenas
    os pares, na ordem que se encontravam'''
    if a%2 == 0:
        filtroa = (a,)
    else:
        filtroa = ()
    if b%2 == 0:
        filtrob = (b,)
    else:
        filtrob = ()
    if c%2 == 0:
        filtroc = (c,)
    else:
        filtroc = ()
    if d%2 == 0:
        filtrod = (d,)
    else:
        filtrod = ()
    return filtroa + filtrob + filtroc + filtrod