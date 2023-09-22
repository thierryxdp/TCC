def media_matriz(matriz):
    """Retorna a media de todos s numeros da matriz com exatamente duas
    casas decimais de precisao, dado: uma matriz de inteiros nao vazia"""
    
    n = 0
    d = len(matriz[0])*len(matriz)
    
    for i in range(len(matriz)):
        n = n+sum(matriz[i])
            
    return round(n/d,2)