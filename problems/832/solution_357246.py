def eh_quadrada(m):
    '''Função que se inserida uma matriz 
    (incluindo uma matriz vazia, que é quadrada) retorna True se a matriz
    é quadrada e False se não o for. list -> bool'''
    i = 0
    k = 0
    while i <=  len(m):
        while k <= len(m):
            if len(m) == len(m[i]):
                x = True
            else:
                x = False
            k = k + 1
        i = i + 1
    if m == None:
        return True
    return x