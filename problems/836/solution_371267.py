def busca(Procurar, matriz): 
    if Procurar not in matriz[0]:
        return []
    for linha in matriz:
        for coluna in linha:
            if coluna == Procurar:
                return [linha]