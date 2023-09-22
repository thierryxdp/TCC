def media_matriz(matriz):
    soma=0
    total_numero=0
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            soma=soma+matriz[i][j]
            total_numero+=1
    media=soma/total_numero 
    return round(media,2)