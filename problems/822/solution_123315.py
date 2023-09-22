def repetidos(lista):
    i = 0
    listaposicoes = 0
    while i<len(lista):
        if lista[i+1] == lista[i]:
            listaposicoes += 1
        i += 1
    return listaposicoes