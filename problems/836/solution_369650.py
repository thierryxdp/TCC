def busca(setor,matriz):
    
    novaMatriz= []
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz[0])):
            if setor == matriz[i][j]:
            linha.append(matriz[i])
        novaMatriz.append(linha)
        
        
    return novaMatriz