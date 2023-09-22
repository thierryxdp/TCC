def media_matriz(matriz):
    soma=0
    divisao=0
    
    nlin=0
    while nlin < len(matriz):
        ncol=0
        while ncol < len(matriz[0]):
            soma= soma + matriz[nlin][ncol]
            divisao += 1
            ncol+=1
        nlin+= 1
    return soma/divisao