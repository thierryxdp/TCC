def insere(lista_numero,n):
    """Esta funcao recebe uma lista e um elemento, adiciona esse elemento na lista e a organiza str -> str"""
    lista_numero.insert(0,n)
    lista_numero.sort()
    return lista