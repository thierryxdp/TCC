def conta_numero(numero, matriz):
    
    contador = 0
    
    for i in matriz:
    	for dado in i:
            if dado == numero:
                contador += 1
                
	return contador