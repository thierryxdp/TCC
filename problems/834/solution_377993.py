def media_matriz(lista):
    """função que dada uma matriz de inteiros nao vazia retorna a média de todos os numeros
    da matriz( com exatamente duas casas decimais de precisão):
    list(list) -> float"""
    
    media = 0
    somatorio = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            somatorio = somatorio + matriz[i][j]
            total = len(matriz[0]) + len(matriz)
            media = somatorio/total
            
    return media