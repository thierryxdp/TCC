def conta_numero(numero,matriz):
    '''Função que dado um número e a matriz qualquer,
conta e retorna quantas vezes o número aparece na matriz.
    int, list -> int'''
    
    contagem = []
    i=0
    
    for linha in range(matriz):
        for coluna in range(linha):
        	if coluna[i] == numero:
            	contagem.append(i)
			i+=1
	return len(contagem)