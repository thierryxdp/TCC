def media_matriz(matriz: int) -> float:
    """Essa função, dada uma matriz de números inteiros não vazias,
    retorna a média de todos os números da matriz com precisão 
    de duas casas decimais"""
    numeros = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numeros.append(matriz[i][j])
    
    media = sum(numeros)/len(numeros)
    
    return round(media,2)