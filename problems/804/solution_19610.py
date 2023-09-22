def filtra_pares(p):
    '''função que recebe uma tupla com 4 elementos inteiros e retorna uma nova tupla contendo,apenas, os elementos pares da tupla original,na mesma ordem em que se encontravam;tuple -> tuple'''
    tupla=()
    if p[0]%2==0:
        tupla=tupla+(p[0],)
    if p[1]%2==0:
        tupla=tupla+(p[1],)
    if p[2]%2==0:
        tupla=tupla+(p[2],)
    if p[3]%2==0:
        tupla=tupla+(p[3],)
    return tupla