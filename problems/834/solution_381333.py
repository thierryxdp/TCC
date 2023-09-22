def media_matriz(matriz):
    result=0
    for linha in matriz:
        for coluna in linha:
            result=coluna+result
    return result/(len(matriz)+len(matriz[0]))