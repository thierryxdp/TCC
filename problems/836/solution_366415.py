def busca(setor, matriz):
    """ """
    for i in matriz:
        for j in i:
            if j[2] == setor:
                return (j)