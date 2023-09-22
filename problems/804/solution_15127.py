def filtra_pares(x):
    '''Retorna uma tupla com todos os valores pares dados na entrada 
    Tupla->tupla'''
    a=()
    if x[0] % 2 ==0:
        a += (x[0],)
    if x[1] %2 == 0:
        a += (x[1],)
    if x[2] % 2 ==0:
        a += (x[2],)
    if x[3] %2 == 0:
        a += (x[3],)
    return a