def filtra_pares(tupla):
    ''' recebe uma tupla com numeros inteiros e retorna uma nova tupla contendo apenas os numeros pares'''
    '''int-> int'''
    tuplapares = ()
    if tupla[1]%2==0:
        tuplapares = tuplapares[1]
    if tupla[2]%2==0:
        tuplapares = tuplapares[2]
    if tupla[3]%2==0:
        tuplapares = tuplapares[3]
    if tupla[4]%2==0:
        tuplapares = tuplapares[4]
    return tuplapares