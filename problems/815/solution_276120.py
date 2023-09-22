def insere(lista_numero, n):
    lista_nova = [n,]
    for e in lista_numero:
        lista_nova.append(e)
    ordenada = lista_nova.sort()
    return ordenada