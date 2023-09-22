def filtraMultiplos(lista, n):
    '''Calcula e filtra os elementos da lista que sao divi
    siveis pelo numero n
    list, [int,float,complex] -> list'''
    i = 0
    resultado = []
    while i<len(lista):
        if lista[i]%n == 0:
            list.append(resultado, lista[i])
        i = i + 1
    return resultado