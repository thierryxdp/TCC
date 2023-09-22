def media_matriz(matriz):
    cont=0
    div=len(matriz)*len(matriz[0])
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(linha):
        for num in range(linha[i]):
            cont=cont + matriz[i][num]
            return round((cont/div), 2)