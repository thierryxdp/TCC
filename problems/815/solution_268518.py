def insere(lista_numero, n):
    if n in lista_numero:
        return 1
    else:
        lista = list.insert(lista_numero, 0, n)
        listaord = lista_numero.sort
        return listaord