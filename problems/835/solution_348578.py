def melhor_volta(m):
    """Função que recebe uma matriz 6x10 e retorna uma tupla com
    a coluna, o menor valor, e a linha.
    lista --> tupla"""
    melhor = m[0][0]
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] < melhor:
                melhor = m[i][j]
                r = (i+1,melhor,j+1)
	return r