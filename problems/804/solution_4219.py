def filtra_pares (n):
    '''recebe uma tupla com 4 elementos inteiros e retorna uma nova
    tupla apenas contendo elementos pares da tupla original'''
    npares = ()
    if n[0]%2 == 0:
        npares+=(n[0],)
    if n[1]%2 == 0 :
        npares+=(n[1],)
    if n[2]%2 == 0:
        npares+=(n[2],)
    if n[3]%2 == 0:
        npares+=(n[3],)
    return npares