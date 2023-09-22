def maiores(lista,n):
    type(lista) == list and type(n) == int
    lista.append(n)
    lista_ordenada=sorted(lista)
    return lista_ordenada