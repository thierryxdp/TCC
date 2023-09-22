def insere(lista,n):
    """Função recebe uma lista e um elemento, adiciona 
    esse elemento na lista e a organiza
    str->str"""
    lista.insert(0,n)
    lista.sort()
    return lista