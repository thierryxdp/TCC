def busca(setor,matriz):
    """..."""
    resp = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == setor:
                resp.append(0)
                resp[i] = []
                resp.append(matriz[i][j])
                
        if setor not in matriz[i][j]:
                return []
    return resp