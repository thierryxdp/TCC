def conta_numero(numero,matriz):
    '''conta a quantidade de ocorrências de um número numa
    matriz; list -> int'''
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        qtd = 0
        for j in range(colunas):
			if numero == matriz[i][j]:
            	qtd += 1
        return qtd