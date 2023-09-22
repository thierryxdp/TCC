def busca(setor,matriz):
    """..."""
    resp = []
    
    for i in range(len(matriz)):
        teste = False
        for j in range(len(matriz[0])):
            if matriz[i][j] in setor:
                teste = True 
        if teste == True:
            for i in range(len(matriz)):
                for j in range(len(matriz[0])):
                    resp.append(matriz[i][j])
                
        if setor not in matriz[i][j]:
                return []
    return resp