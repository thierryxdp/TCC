def busca(setor,matriz):
    
    dados = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][2] == busca:
                dados += [matriz[i]]
    return dados