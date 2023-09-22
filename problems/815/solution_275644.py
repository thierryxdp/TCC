def insere(lista_numero,n):
    """ Retorna uma nova lista ordenada com a inserção do numero n, dado o numero e uma lista; lista,int--> lista"""
    lista_numero = list.append(lista_numero,n)
    lista_numero = list.sort(lista_numero)
    return lista_numero