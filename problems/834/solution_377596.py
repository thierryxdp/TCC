def media_matriz (matriz:list) -> float:
    """Função que dada uma matriz de números inteiros não vazia, retorna a média de todos os números da matriz, com exatamente duas casas decimais de precisão."""
    numeros = 0
    soma = 0
    for i in range (len (matriz)):
        for j in range (len (matriz[0])):
            soma += matriz[i][j] 
            numeros += 1
    return round((numeros/denominador),2)