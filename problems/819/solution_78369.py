def filltraMultiplos(lista,n):
    """..."""
    resposta = lista[]
    n_elementos = len(lista)
    indice = 0 
    while (indice<n_elementos):
        if (lista[indice] % n == 0):
            resposta += (lista[indice],)

        indice += 1

    return resposta