def media_matriz(matriz):
    """A funcao calcula a media dos numeros dentro da matriz dada como entrada
    , o resultado será arredondado para duas casas decimais.list(matriz)-->float """
    qntd = len(matriz)*len(matriz[0])
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma = soma + matriz[i][j]
    return round(soma/qntd,2)