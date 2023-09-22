def insere(lista_numero,n):
    for x in range(len(lista_numero)):
        if n>lista_numero[x] and n not in lista_numero:
            lista_numero.insert(n,x+1)
    return lista_numero