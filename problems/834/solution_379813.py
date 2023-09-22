def media_matriz(matriz):
    """
    recebe uma matriz e retorna a media de todos os seus numeros
    """
    
    soma=0
    qelem=0
    for linha in matriz:
        for elem in linha:
            soma+=elem
            qelem+=1
    return round(soma/qelem,2)