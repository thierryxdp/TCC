def filtra_pares(tuple):
    '''função que dada uma tuple de 4 elementos retorna uma tuple
    com os inteiros pares da tuple original, mantando a ordem dos 
    elementos, tuple->tuple'''
    pares=()
    if tuple[0]%2 == 0:
        pares+=tuple[0]
    if tuple[1]%2 == 0:
        pares+=tuple[1]
    if tuple[2]%2 == 0:
        pares+=tuple[2]
    if tuple[3]%2 == 0:
        pares+=tuple[3]
    if tuple[4]%2 == 0:   
        pares+=tuple[4]
    return pares