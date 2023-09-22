def busca(setor,matriz):
    
    dados = []
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            dados += [matriz[i]]
    return dados