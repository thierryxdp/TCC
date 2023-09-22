def media_matriz(matriz):
    """finção que dada uma matriz retorna a media de todos os numeros
    list -> float"""
    soma_matriz = sum(matriz)
    
    nlin = len(matriz)
    ncol = len(matriz[0])
    
    tamanho = nlin * ncol
    
    return soma_matriz/tamanho