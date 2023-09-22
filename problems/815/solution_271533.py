def insere(lista_numero,n):
    '''retorna a lista com a adicao do numero n; list, int -> list'''
    lista_com_m = lista_numero + [n]
    list.sort(lista_com_m)
    return lista_com_m