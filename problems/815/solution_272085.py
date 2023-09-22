def insere(lista_numero, n):
    list.sort(lista_numero)
    list.reverse(lista_numero)
    list.insert(lista_numero, list.index(n),n)
    return lista_numero