from math import*
def filtra_pare(tupla_inteiros): 
    '''Função que retorna uma tupla contendo apenas os numeros pares, dada uma tupla com 4 numeros inteiros'''
    lista_pares = []
    if tupla_inteiros[0] % 2 == 0:
        lista_pares.append(tupla_inteiros[0])
    if tupla_inteiros[1] % 2 == 0:
        lista_pares.append(tupla_inteiros[1])
    if tupla_inteiros[2] % 2 == 0:
        lista_pares.append(tupla_inteiros[2])
    if tupla_inteiros[3] % 2 == 0:
        lista_pares.append(tupla_inteiros[3])

    lista_pares = tuple(lista_pares)