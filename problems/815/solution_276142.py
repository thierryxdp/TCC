def insere(lista_numero,n):
    for x in range(len(lista_numero)):
        if n>lista_numero[x] and n not in lista_numero:
            lista_numero.insert(x+1,n)
            lista_numero.sort
    return lista_numero