def filtra_pares(x):
    ''' Recebe uma tupla com 4 elementos inteiros e retorna uma nova tupla contendo apenas os números pares da tupla original.
    tupla->tupla'''
    tupla=()
    if x[0]%2==0:
        tupla= tupla +(x[0],)
    if x[1]%2==0:
        tupla= tupla +(x[1],)
    if x[2]%2==0:
        tupla= tupla +(x[2],)
    if x[3]%2==0:
        tupla= tupla +(x[3],)
    return tupla