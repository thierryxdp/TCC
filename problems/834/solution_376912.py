def media_matriz(matriz): 
    contador=0
    for linha in matriz:
        for elemento in linha:
            	contador=contador+elemento
    return contador/len(matriz)