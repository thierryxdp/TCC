def filtra_pares(numeros):
    '''recebe uma tupla com quatro elementos inteiros, e retorna uma tupla contendo apenas os elementos
pares da tupla digitada, em sua respectiva ordem.
tupl -> tupl'''
    lista = []
    for n in numeros:
        if n % 2 == 0:
            lista.append(n)
    return lista