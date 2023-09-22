def media_matriz(matriz):
    """retorna a media de todos os numeros da matriz"""
    c=0
    s=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            c+=1
            s=s+matriz[i][j]
    return round(s/c,2)