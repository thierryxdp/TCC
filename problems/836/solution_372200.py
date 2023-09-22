def busca(setor, matriz):

    dados = []
    
    for i in range(len(matriz)):
        if setor in matriz[i]:
            dados.append(matriz[i])

    return dados