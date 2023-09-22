def media_matriz(matriz):
    """Dada uma matriz de inteiros não vazia, a função retorna a média
    aritmética de todos os números da matriz com 2 casas decimais.
    matriz -> float"""
    
    soma = 0
    linhas = len(m)
    colunas = len(m[0])
    total_de_numeros = linhas*colunas
    
    for i in range(linhas):
        for j in range(colunas):
            numero = matriz[i][j]
            soma = soma + numero
            
	return round((soma/total_de_numeros), 2)