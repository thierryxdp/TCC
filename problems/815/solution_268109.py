def insere(lista_numero,n):
    '''
    a função retorna a lista ordenada com
    o numero inserido.
    list,int -> list
    '''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero