def _maiores(lista_numero, n):
    lista_numero.append(n)
    list.sort(lista_numero)
    lista_numero.del(:n)
    return lista_numero