def conta_numero(numero, matriz):
    '''
    	essa função recebe uma matriz qualquer e um numero inteiro e retorna a quantidade
        de vezes que esse número aparece dentro da matriz
        num, list -> num
    '''
    
    for x in matriz:
        qntd = 0
        for y in x:
            if y == numero:
                qntd = qntd+1
    return qntd
		else:
        	return 0