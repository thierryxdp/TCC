def busca(Procurar, matriz):
    lista = []
    for linha in matriz:
        for coluna in matriz:
            if Procurar not in coluna:
                lista += [coluna]
        return lista