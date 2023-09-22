def filtra_pares(a,b,c,d):
    if a%2 == 0:
        restoa = 1
    else:
        restoa = 0
    if b%2 == 0:
        restob = 1
    else:
        restob = 0
    if c%2 == 0:
        restoc = 1
    else:
        restoc = 0
    if d%2 == 0:
        restod = 1
    else:
        restod = 0
    lista1 = {restoa: a,
              restob: b,
              restoc: c,
              restod: d}
    return lista1[1]