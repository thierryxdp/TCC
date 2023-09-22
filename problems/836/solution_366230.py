def busca(matriz, setor):
    """ """
    for i in matriz:
        for j in i:
            if setor in j:
                return matriz[i]