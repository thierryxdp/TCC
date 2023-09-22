def media_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    listanum = []
    soma_lista = list.sum(listanum) 
    media = soma_lista/linhas*colunas
    
    for i in range(linhas):
        for j in range(colunas): 
            listanum += matriz[i][j],
           
    return round(media,2)