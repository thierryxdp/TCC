def media_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    listanum = []
    
    for i in range(linhas):
        for j in range(colunas): 
            listnum += matriz[i][j]
           
    return round(listnum.sum()/linhas*colunas,2)