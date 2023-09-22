def filtra_pares(numeros):
    '''recebe uma tupla com quatro elementos inteiros, e retorna uma tupla contendo apenas os elementos
pares da tupla digitada, em sua respectiva ordem.
tupl -> tupl'''
    lista_pares = []
    for n in numeros:
            if n % 2 == 0:
                lista_pares.append(n)
                return lista_pares