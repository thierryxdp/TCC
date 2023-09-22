def faltante(lista):
    n = len(lista) + 1
    novaLista = list(range(n))[1:len(lista) + 1]
    listaRetorno = []
    i = 0

    while i < len(lista):
        if lista[i] != novaLista[i]:
            listaRetorno.append(i)
        i += 1

    return listaRetorno[0] + 1