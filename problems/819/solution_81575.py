def filtraMultiplos(lista, n):
    '''crie uma função que filtre, de uma lista dada como entrada, os múltiplos de um número n em form de uma nova lista. list,int-->list.'''
    lista_multiplos = []
    i = 0
    n = int(n)
    while i < len(lista):
        if lista[i]%n == 0:
            lista_multiplos = lista_multiplos + [lista[i],]
        i = i + 1
    return lista_multiplos