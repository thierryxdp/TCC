def busca(setor,matriz):
    
    dados = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            matriz[i].remove(matriz[i][2])
            dados += [matriz[i]]
    return dados