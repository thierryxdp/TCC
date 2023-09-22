def busca(setor,matriz):
    
    dados = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
            funcionario = [matriz[i][0],matriz[i][1],matriz[i][2]]
            dados += funcionario
    return dados