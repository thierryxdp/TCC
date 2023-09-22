def conta_numero(numero, matriz):
    ''' Conta a quantidade de (numero) em uma determinada
    (matriz)
    int, list -> int'''
    contador = 0
    
    for i in matriz:
    	for dado in i:
            if dado == numero:
                contador += 1
                
	return contador