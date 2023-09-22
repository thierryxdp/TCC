def repetidos(lista):
    i=1
    repete=0
    while i<len(lista):
   		#elemento da lista é igual ao anterior
    	if lista[i]==lista[i-1]:
    		repete+=1
        i+=1
    return repete