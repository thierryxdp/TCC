def busca(setor,matriz):
    
    novaMatriz= []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if setor == matriz[i][j]:
                novaMatriz.append(matriz[i])
        
    print (novaMatriz)    
    return novaMatriz