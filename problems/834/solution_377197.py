def media_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    listanum = []
    
    for i in range(linhas):
        for j in range(colunas): 
            listanum += matriz[i][j],
           
    return round(listanum.sum()/linhas*colunas,2)