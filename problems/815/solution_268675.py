def insere(lista_numero, n):
    lista_numero.sort()
    primeiro_numero = lista_numero[0]
    lista_numero.insert(n - primeiro_numero, n)
    return lista_numero