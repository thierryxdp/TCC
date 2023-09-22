def filtra_pares (a, b, c, d):
    'Funcao que recebe uma tupla com quatro elementos inteiros'
    'como parametros e retorna uma nova tupla contendo apenas os'
    'elementos pares da tupla original, na mesma ordem'
    'em que se encontravam'
    
    tup = (a, b, c, d)
    if a%2, b%2, c%2, d%2 == 0:
        return tup
    elif b%2, c%2, d%2 == 0:
        return tup [1:]
    elif c%2, d%2 == 0:
        return tup [2:]
    elif d%2 == 0:
        return tup [3:]
    else:
        return []