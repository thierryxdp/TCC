def filtra_pares (a, b, c, d):
    'Funcao que recebe uma tupla com quatro elementos inteiros'
    'como parametros e retorna uma nova tupla contendo apenas os'
    'elementos pares da tupla original, na mesma ordem'
    'em que se encontravam'
    
    
    if a%2 == 0 and b%2 == 0 and c%2 == 0 and d%2 == 0:
        return (a, b, c, d)
    if a%2 == 0 and b%2 == 0 and c%2 == 0:
        return (a, b, c)
    if a%2 == 0 and b%2 == 0 and d%2 == 0:
        return (a, b, d)
    if b%2 == 0 and c%2 == 0 and d%2 == 0:
        return (b, c, d)
    if a%2 == 0 and b%2 == 0:
        return (a, b)
    if a%2 == 0 and c%2 == 0:
        return (a, c)
    if a%2 == 0 and d%2 == 0:
        return (a, d)
    if b%2 == 0 and c%2 == 0:
        return (b, c)
    if b%2 == 0 and d%2 == 0:
        return (b, d)
    if c%2 == 0 and d%2 == 0:
        return (c, d)
    if a%2 == 0:
        return (a)
    if b%2 == 0:
        return (b)
    if c%2 == 0:
        return (c)
    if d%2 == 0:
        return (d)
    else:
        return ()