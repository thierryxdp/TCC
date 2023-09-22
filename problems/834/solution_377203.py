def media_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    listanum = []
    
    
    for i in range(linhas):
        for j in range(colunas): 
            listanum += matriz[i][j],
    soma_lista = sum(listanum) 
    
    media = soma_lista/linhas*colunas
           
    return round(media,2)