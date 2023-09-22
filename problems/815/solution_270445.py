def insere(lista_numero,n):
    """ Essa função recebe uma lista e um número n e or
    dena essa lista para depois inserir n na posição correta.
    lista,int-> lista."""
    listanova = list.append(lista_numero,n)
    lista2 = list.sort(listanova)
    return listanova