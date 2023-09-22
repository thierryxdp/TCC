def eh_quadrada(m):
    '''Função que se inserida uma matriz 
    (incluindo uma matriz vazia, que é quadrada) retorna True se a matriz
    é quadrada e False se não o for. list -> bool'''
    for i in m:
        for k in m[i]:
            if len(m) == len(m[i]):
                x = True
        else:
            x = False
    if m == None:
        return True
    return x