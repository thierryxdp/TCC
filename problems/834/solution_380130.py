def media_matriz(matriz):
    """
    lista->float"""
    
    contador = 0
    media = 0
    soma = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soma = soma + matriz[i][j]
            contador += 1
    media = soma/contador
    
    return media