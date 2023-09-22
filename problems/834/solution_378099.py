def media_matriz(matriz: list) -> float:
    """ Função que dada uma matriz de inteiros não vazia, retorna a média
    de todos os números da matriz (com exatamente duas casas decimais de
    precisão.
    list(list)->float """
    
    soma=0
    divisor=0
    
    for i in range(len(matriz)):
        
        for j in range(len(matriz[i])):
            soma+= matriz[i][j]
            divisor+= 1
                    
    media= soma/divisor
    media= round(media,2)
    return media