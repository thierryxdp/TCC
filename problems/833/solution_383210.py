def conta_numero(numero,matriz):
    '''Função que recebe um inteiro e uma matriz de inteiros, conta e retorna a 
    quantidade de ocorrências desse número na matriz'''
    '''int, list(list(int)) -> int'''
    qts_aparece = 0
    i = 0
	while i < len(matriz):
        for n in matriz[i]:
            if numero == n:
            	qts_aparece = qts_aparece + 1
            	i = i + 1
        else: 
            i = i + 1
	return qts_aparece