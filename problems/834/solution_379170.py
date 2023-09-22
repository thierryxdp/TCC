def media_matriz(matriz):
    diviisor=len(matriz)*len(matriz[0])
    soma=0
    for linha in range(len(matriz)):
        for indice in range(len(matriz[linha])):
            soma=soma+matriz[linha][indice]
            divida=soma/diviisor arredonda=round(divida, 2)
            return