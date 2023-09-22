def repetidos(lista):
    '''
    	
	'''
    i=0
    at=0
    post=0
    acumulador=0
    while (i<len(lista)):
        post=i+1
        anter=i-1
        if (i==0):
            break
        if (post==len(lista)) and (lista[anter]==lista[i]):
            acumulador+=1
        if lista[i]== lista[anter]:
            acumulador+=1
    	i+=1
    
    return acumulador