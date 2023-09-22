def media_matriz(matriz):
    '''
    Retorna a media dos numeros da matriz com duas casas decimais
        Parametros:
            matriz: list
        Saida: float
    '''
    soma = 0

    cont = 0

    for i in range(len(matriz)):
        soma += sum(matriz[i])

    cont += len(matriz[i])

    return round((soma/cont),2)