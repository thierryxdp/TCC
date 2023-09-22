def media_matriz(matriz):

    soma = 0.
    cont = 0
    
    for i in matriz:
        for j in i:
            soma = soma + j
            cont = cont + 1
    media = soma/cont
    return media