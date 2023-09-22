def repetidos (lista):
	repetidas = 0
	for i in lista:
    	if lista[i] == lista[i+1]:
       	 	repetidas+=1
	return repetidas