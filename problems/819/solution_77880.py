def filtraMultiplos(lista, n):
    ''' Função que retorna os múltiplos do número n que pertencem à lista 
    list, int -> list '''
    i = 1
    divisiveis = []
    while i < len(lista):
        if list[i] == list[i-1]:
            list.append(divisiveis, lista[i])
            i = i+1
        else:
            i = i+1
    return divisiveis