def media_matriz(matriz:list)-> float:
    """Função que, dada uma matriz de inteiros
    não vazia, retorna a média de todos
    os números da matriz."""
    
    soma = 0
    quant_numeros = 0
    linhas = len(matriz)
    
    for i in linhas:
        coluna = matriz[i]
        for numero in coluna:
            soma += numero
            quant_numeros +=1
    media = soma/quant_numeros
    
    return round(media,2)