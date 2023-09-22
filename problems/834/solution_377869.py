def media_matriz(m):
    """
    Função que recebe uma matriz de inteiros nao vazia e retorna a média com duas casas decimais de todos os números da matriz.
    Parâmetro:
    	m: list
    Saída:
    	float
    """
    soma = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            soma += m[i][j]
    return round(soma/(len(m)*len(m[0])), 2)