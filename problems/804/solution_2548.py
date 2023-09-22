def filtra_pares (t):
    """ recebe uma tupla 't' de quatro elementos e retorna uma nova tupla
    contendo apenas os elementos pares da tupla original
    tuple -> tuple """
    pares=()
    if t[0]%2==0: pares = pares + (t[0],) or t[1]%2==0 pares = pares + (t[1],)
    or t[2]%2==0:pares = pares + (t[2],) or t[3]%2==0:pares = pares + (t[3],)
    return pares