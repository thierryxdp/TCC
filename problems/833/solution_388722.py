def conta_numero(numero,matriz):
    '''dado um numero e uma matriz a funcao retorna
    quantas vezes o numero aparece dentro da matriz
    int,matriz -->int'''
    contador = 0
    for i in matriz:
        for k in i:
            if k == numero:
                contador += 1
	return contador