def filtraMultiplos(numlist, n):
    '''funcao que dada uma lista de numeros e um numero n, retorna uma lista com os numeros da lista
       divisiveis por n
       list, float -> list '''
    indice = 0
    divisiveis = []
    while (indice < len(numlist)):
        if (numlist[indice]%n == 0):
            list.append(divisiveis, numlist[indice])
        indice += 1
    return divisiveis