def repetidos (lista):
	repetidas = 0
	for i in range(1, Len(lista)+1):
    	if lista[i] == lista[i-1]:
       	 	Repetidas+=1
	return repetidas