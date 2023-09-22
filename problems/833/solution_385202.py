def conta_numero(numero, matriz):
    QuantidadeVezes = 0
   	for linha in matriz:
    	for coluna in linha:
            if numero == coluna:
                QuantidadeVezes += 1
	return QuantidadeVezes