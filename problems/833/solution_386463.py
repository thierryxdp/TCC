def conta_numero(n,matriz):
    """ função que conta quantos números n tem na matriz"""
    soma = 0
    for i in range (len(matriz)):
        for j in (matriz[i]):
            if j==n:
                soma += 1
	return soma