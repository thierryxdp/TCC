def media_matriz(matriz):
    soma = 0
    contador = 0
    for i in matriz:
        for j in i:
            soma += j
            contador += 1
    media_matriz = round(soma/contador,2)
         
    return media_matriz