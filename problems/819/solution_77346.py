def filtraMultiplos(lista,n):
    '''função que retorna uma lista contendo todos os elementos
    da lista de entrada que forem divisíveis por n
    list, int -> list'''
    i = 0
    nova_lista = []
    while i < len(lista):
        if lista[i] % n == 0:
            list.append(nova_lista,lista[i])
        i += 1
    return nova_lista