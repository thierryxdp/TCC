def filtraMultiplos(lista, n):
    ''' Função que filtra os números da lista que são divisíveis pelo número dado 
    list, int -> int '''
    i = 0
    divisiveis = []
    while i < len(lista):
        if lista[i]%n == 0:
            list.append(divisiveis, lista[i])
            i = i+1
    return divisiveis