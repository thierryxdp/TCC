def insere(lista_numero,n):
    """função que retorna uma lista ordenada
    list,int -> list"""
    list.insert(lista_numero,0,n)
    list.sort(lista_numero)
    return lista_numero