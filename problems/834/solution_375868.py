def media_matriz(matriz):
    """Calcula e retorna a média de todos os números da matriz dada;
       list->float
       Parâmetro:
       matriz: uma matriz não vazia
    """
    soma=0
    divisor=[]
    for i in range(len(matriz)):
        for num in range(len(matriz[i])):
            elemento=matriz[i][num]
            div.append(elemento)
            soma=soma+elemento
    media=soma/len(divisor)
    return round(media,2)