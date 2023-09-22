def conta_numero(numero, matriz):
    '''Dado um número inteiro e uma matriz de inteiros, retorna 
    quantas vezes aquele número aparece na matriz.
    int, list -> int'''
    acumul = 0
    for linha in matriz: 
		acumul += list.count(linha,numero)
	return acumul