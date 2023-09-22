def filtra_pares(tupla):
    ''' recebe uma tupla com numeros inteiros e retorna uma nova tupla contendo apenas os numeros pares'''
    '''int-> int'''
    tuplapares = ()
    if tupla[0]%2==0:
        tuplapares = tuplapares + (tupla[0])
    if tupla[1]%2==0:
        tuplapares = tuplapares + (tupla[1])
    if tupla[2]%2==0:
        tuplapares = tuplapares + (tupla[2])
    if tupla[3]%2==0:
        tuplapares = tuplapares + (tupla[3])
    return tuplapares