def insere(lista_numero, n):
    for numero in lista_numero:
        if n > numero:
            lista_numero.insert(lista_numero.index(numero) + 1, n)
        else:
            lista_numero.insert(lista_numero.index(numero), n)
    return lista_numero