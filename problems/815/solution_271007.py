def insere(lista_numero,n):
    '''
    list,int ---> list
    retorna nova lista ordenada com o elemento fornecido
    '''
    lista = lista_numero + [n]
    lista.sort()
    return lista