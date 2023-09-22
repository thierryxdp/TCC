insere(lista_numero,n):
    for x in range(len(lista_numero)):
        if n>lista_numero[x] and n not in lista_numero:
            list.insert(n, lista_numero)
    return lista_numero