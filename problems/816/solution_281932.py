def maiores(lista,n):
    '''Retorna lista contendo os numeros maiores que n da lista de entrada, em ordem crescente.
    list,int->list'''
    nova_lista=lista[:]
    list.append(nova_lista,n)
    list.sort(nova_lista)
    del nova_lista[list.index(nova_lista,n):]
    return nova_lista