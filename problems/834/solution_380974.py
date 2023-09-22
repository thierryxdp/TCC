def media_matriz(matriz):
    i=0
    soma=0
    quantidade=0
    while i <len(matriz):
        j=0
        while j<len(matriz[i]):
            soma= soma+matriz[i][j]
            quantidade = quantidade+1
            j=j+1
        i =i+1
    media= soma/quantidade 
    return round (media,2)