def media_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    listanum = []
    media = soma_lista/linhas*colunas
    
    for i in range(linhas):
        for j in range(colunas): 
            listanum += matriz[i][j],
        soma_lista = sum(listanum) 
           
    return round(media,2)