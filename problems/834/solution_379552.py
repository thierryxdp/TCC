def media_matriz(m):
    """
    Rteorna a média dos números da matriz.
    list -> float
    """
    numeros=[]
    for i in range(len(m)):
        for j in range(len(m[0])):
            numeros += m[i][j]
    media= round(numeros/len(numeros),2)
    return media