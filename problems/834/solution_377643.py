def media_matriz(matriz: list)-> float:
    """Dada uma matriz de número inteiros não vazia, retorna
    a média dos números da matriz."""
    linhas = len(matriz)
    colunas = len(matriz[0])
    soma = 0
    qtd_numeros = 0
    
    for i in range(linhas):
        for j in range(colunas):
            soma += matriz[i][j]
            qtd_numeros += 1
    media = soma / qtd_numeros
    
    return round(media,2)