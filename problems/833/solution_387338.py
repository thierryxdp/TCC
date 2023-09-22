def conta_numero(numero, matriz):
	'''esta função percorre a matriz inteira e verifica se há numero
   	int, list--> int '''
    ttl = 0
    for item in matriz:
        for item2 in item:
            if item2 == numero:
                ttl += 1

    return ttl