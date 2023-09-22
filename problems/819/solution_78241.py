def filtraMultiplos(lista,n):
    '''A partir da lista de numeros fornecida retorna
    uma lista com os elementos da lista que sao multiplos
    do numero n
    list,int'''
    multiplos = []
    k = 0
    while k < len(lista):
        if (lista[k])%(n) == 0:
            list.append(multiplos,lista[k])
      	k = k + 1
    return multiplos