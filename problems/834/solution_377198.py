def media_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    listanum = []
    media = listanum.sum()/linhas*colunas
    
    for i in range(linhas):
        for j in range(colunas): 
            listanum += matriz[i][j],
           
    return round(media,2)