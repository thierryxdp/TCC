def filtra_pares(tupla):
    '''Recebe uma tupla de numeros inteiros e retorna
    uma nova tupla contendo apenas os números pares
    da tupla original
    tuple -> tuple'''
    novaTupla = ()
    if tupla[0] // 2 == 0:
        novaTupla = tupla[0]
    if tupla[1] // 2 == 0:
        novaTupla = tupla[1]
    if tupla[2] // 2 == 0:
        novaTupla = tupla[2]
    if tupla[3] // 2 == 0:
        novaTupla = tupla[3]
    return novaTupla