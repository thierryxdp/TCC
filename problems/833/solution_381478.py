def conta_numero(numero,matriz):
    '''Função que dado um número e a matriz qualquer,
conta e retorna quantas vezes o número aparece na matriz.
    int, list -> int'''
    
    contagem = []
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    for i in range(linhas):
        for j in range(colunas):
            if j == numero:
                contagem.append(j)
	return len(contagem)