def insere(lista_numero, n):
    for numero in lista_numero:
        if n > numero:
            lista_numero.insert(n, lista_numero.index(numero))
    return lista_numero