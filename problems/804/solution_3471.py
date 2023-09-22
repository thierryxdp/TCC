def filtra_pares (a, b, c, d):
    'Funcao que recebe uma tupla com quatro elementos inteiros'
    'como parametros e retorna uma nova tupla contendo apenas os'
    'elementos pares da tupla original, na mesma ordem'
    'em que se encontravam'
    
    tup = a, b, c, d
    if a%2 == 0 and b%2 == 0 and c%2 == 0 and d%2 == 0:
        return tup
    if b%2 ==0 and c%2 ==0 and d%2 == 0:
        return tup [1:]
    if c%2 ==0 and d%2 == 0:
        return tup [2:]
    if d%2 == 0:
        return tup [3:]
    else:
        return []