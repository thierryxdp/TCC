def filtraMultiplos(lista, n):
    ''' Função que retorna os múltiplos do número n que pertencem à lista 
    list, int -> list '''
    i = 0
    divisiveis = []
    while i < len(lista):
        if lista[i]%n == 0:
            list.append(divisiveis, lista[i])
            i = i+1
        else:
            i = i+1
    return divisiveis