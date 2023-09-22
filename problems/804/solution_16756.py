def filtra_pares(v):
    '''
    Recebe uma tupla com 4 valores inteiros determinados.
    Abre uma tupla vazia. Adiciona os valores na ordem,
    caso eles sejam considerados pares.
    tuple -> tuple
    '''
    a = ()
    b = ()
    c = ()
    d = ()
    
    if v[0] % 2 == 0:
        a = (v[0],)
    if v[1] % 2 == 0:
        b = (v[1],)
    if v[2] % 2 == 0:
        c = (v[2],)
    if v[3] % 2 == 0:
        d = (v[3],)
    return a+b+c+d