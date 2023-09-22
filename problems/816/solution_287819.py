def _maiores(lista_numero, n):
    lista_numero.append(n)
    list.sort(lista_numero)
    lista_numero.del(0:n:1)
    return lista_numero