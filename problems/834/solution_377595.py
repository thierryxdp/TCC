def media_matriz (matriz:list) -> float:
    """Função que dada uma matriz de números inteiros não vazia, retorna a média de todos os números da matriz, com exatamente duas casas decimais de precisão."""
    numeros = 0
    denominador = len (numeros)
    for i in range (len (matriz)):
        for j in range (len (matriz[0])):
            numeros += matriz[i][j] 
    return round((numeros/denominador),2)