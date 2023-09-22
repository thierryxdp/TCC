def filtraMultiplos (lista, numero):
    '''Funcao que recebe uma lista e um numero e retorna outra lista com os numeros divisiveis por n'''
    ''' list, int -> int'''
    lista1 = [lista]
    lista3 = []
    multiplo = 0
    for valor in lista:
        if valor//numero = 0:
            multiplo = valor
            lista3.append(valor)
    return lista3