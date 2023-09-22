def repetidos (lista):

lista.sort()    
cont = 0
	for i in range(len(lista)):
		 if (lista[i] == lista[i+1]):
				 cont += 1
                    
                    
	return cont