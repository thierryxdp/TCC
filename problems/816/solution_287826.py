def _maiores(lista_numero, n):
    lista_numero.append(n)
    list.sort(lista_numero)
    x=lista_numero.index(n)
    lista_numero.del(:x)
    return lista_numero