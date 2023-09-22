def insere(lista_numero,n):
    """retorna a lista com n inserido na ordem
    list,int->list"""
    lista_numero.insert(0,n)
    list.sort(lista_numero)
    return lista_numero