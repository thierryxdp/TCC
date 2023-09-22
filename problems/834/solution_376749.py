def media_matriz(matriz):
        soma = 0
        for i in range(len(matriz)):
            soma=soma+sum(matriz[i])
            div=len(matriz)*len(matriz[0])
        total= soma/div
        return round(total,2)