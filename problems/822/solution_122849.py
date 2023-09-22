def repetidos(lista):
    i=0
    contaRepetidos = 0
    
    while i < len(lista):
        if lista[i] == lista[i-1]:
            contaRepetidos += 1
           
		i += 1 
	
    return contaRepetidos