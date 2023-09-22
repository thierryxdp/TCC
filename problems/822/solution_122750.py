def repetidos (lista):
	repetidas = 0
	for i in range(1, len(lista)+1):
    	if lista[i] == lista[i-1]:
       	 	repetidas+=1
	return repetidas