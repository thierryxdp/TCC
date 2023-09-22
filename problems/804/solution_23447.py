def filtra_pares(tp):
    '''A funcao retorna os valores pares da tupla de entrada em ordem'''
    tupla=()
    for i in tp:
        if i%2==0:
            tupla+=(i,)
    return tupla