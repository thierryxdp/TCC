def media_matriz(matriz):
    a=len(matriz)
    b=len(matriz[0])
    soma=map(lambda x: sum(matriz[x]), range(len(matriz)))
    return round(sum(soma)/(a*b),2)