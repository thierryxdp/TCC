def repetidos(lista):
    i = 0
    listaposicoes = 0
    proximo = i+1
    while i<len(lista):
        if lista[proximo] == lista[i]:
            listaposicoes += 1
        i += 1
    return listaposicoes