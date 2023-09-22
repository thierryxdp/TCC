def insere(lista_numero,n):
    """ Essa função recebe uma lista e um número n e or
    dena essa lista para depois inserir n na posição correta.
    lista,int-> lista."""
    lista_numero.append(n)
    lista_numero.sort(reverse = False)
    return lista_numero