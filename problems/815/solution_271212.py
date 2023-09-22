def insere(lista_numero,n):
    '''função que adiciona um elemento a uma lista e retorna
    a lista ordenada com o elemento no lugar correto
    segundo a ordem crescente
    list,int-> list'''
    lista= lista_numero
    list.insert(lista,0,n)
    list.sort(lista)
    return lista