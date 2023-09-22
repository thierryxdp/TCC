def busca(matriz, setor):
    listaR = []
    for i in matriz:
        if setor == i[2]:
            listaR.append(i)
    return listaR