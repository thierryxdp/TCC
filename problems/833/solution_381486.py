def conta_numero(numero,matriz):
    '''Função que dado um número e a matriz qualquer,
conta e retorna quantas vezes o número aparece na matriz.
    int, list -> int'''
    
    contagem = []
    for linha in matriz:
        for coluna in linha:
        	if numero in coluna:
            	contagem.append(numero)
	return len(contagem)