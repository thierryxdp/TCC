def filtra_pares(tupla):
    '''Recebe uma tupla com quatro elementos inteiros como parâmetro, e retorna uma nova tupla
    contendo apenas os elementos pares da tupla original'''
    lista = []
    for x in tupla:
        if x % 2 == 0 or x == 0:
            lista[len(lista):] = [x]
    return tuple(lista)