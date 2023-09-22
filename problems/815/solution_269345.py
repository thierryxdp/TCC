def insere(lista_numero,n): 
    """ Funcao que retorna uma lista ordenada e um
    numero inteiro n
    list,int->list"""
    
    lista_numero = lista_numero[:] + [n]
    list.sort(lista_numero)
    return lista_numero