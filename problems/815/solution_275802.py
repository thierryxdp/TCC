def insere(lista,n):
    """Esta funcao recebe um elemento e uma lista, adiciona esse elemento na lista e organiza a lista
    entrada: str, saída: str"""
    lista.insert(0,n)
    lista.sort()
    return lista