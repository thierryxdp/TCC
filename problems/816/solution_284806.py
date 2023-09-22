def maiores(lista,n):
    type(lista) == list and type(n) == int
    nova_lista = lista+n
    lista_ordenada=sorted(nova_lista)
    return lista_ordenada