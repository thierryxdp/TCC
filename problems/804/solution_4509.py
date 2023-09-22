def filtra_pares(x):
    num = list(x)
    retorno = []
    a = num[0]
    b = num[1]
    c = num[2]
    d = num[3]
    r = [a%2,b%2,c%2,d%2]
    if r[0] == 0:
        retorno = retorno + [a]
    if r[1] == 0:
        retorno = retorno + [b]
    if r[1] == 0:
        retorno = retorno + [c]
    if r[3] == 0:
        retorno = retorno + [b]
    return retorno