def conta_numero(numero,matriz):
    '''função que dado um número inteiro e uma matriz de inteiros
    retorna quantas vezes aquele número aparece na matriz;
    int,list-->int'''
	quantidade=0
	for linha in matriz:
		quantidade=quantidade+list.count(linha,numero)
	return quantidade