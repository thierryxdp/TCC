def filtraMultiplos(lista, n ):
    novaLista = []
    indice = 0
    tamanhoFinal = len(lista)
    while indice < tamanhoFinal:
        if lista[indice]%n == 0:
            indice = indice + 1
            continue
        novaLista.append(lista[indice])
        indice = indice + 1
    return novaLista