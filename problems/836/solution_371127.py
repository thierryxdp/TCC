def busca(setor,matriz):
    """..."""
    resp = []
    
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            if matriz[i][j] == setor:
                resp.append(0)
                resp[i] = []      
        if setor not in matriz[i][j]:
                return []
    return resp