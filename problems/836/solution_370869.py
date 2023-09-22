def busca(setor, matriz):
    listaR = []
    for i in matriz:
        if setor == i[2]:
            listaR.append([i[0],i[1],i[3])
    return listaR