def filtraMultiplos(lista,numero):
    """ """
    indice = 0
    novaLista = []
    while indice < len(lista):
        if lista[indice] % numero == 0:
            novaLista.append(lista[indice])
        indice += 1
    return novaLista