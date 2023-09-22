def maiores(lista,numero):
    lista.sort()
    indice = lista.index(numero)
    novaLista = lista[indice+1:]
    return novaLista