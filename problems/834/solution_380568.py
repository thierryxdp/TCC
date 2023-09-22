def media_matriz(matriz):
    """
    Essa funcao ira calcular a media dos elementos de uma matriz dada como
    argumento
    list->float
    """
    #contador para divisao
    contador = 0
    soma = 0
    for linha in matriz:
        for num in linha:
            soma += num
            contador +=1
    
    return round(soma/contador,2)