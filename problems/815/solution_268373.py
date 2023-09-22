def insere (lista_numero, n):
    for i, elemento in enumerate(lista_numero):
        if n < elemento:
            lista_numero.insert(i, n)
            return lista_numero