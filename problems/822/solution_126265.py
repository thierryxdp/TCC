def repetidos(lista):
    '''
    	Função que recebe uma lista de números e retorna o número de vezes
        que um elemnto da lista é igual ao elemento anterior.
        list -> list
	'''
    i=0
    at=0
    post=0
    acumulador=0
    while (i<len(lista)):
        post=i+1
        anter=i-1
        if (post==len(lista)) and (lista[anter]==lista[i]):
            acumulador+=1
        if (i!=0) and lista[i]== lista[anter]:
            acumulador+=1
    	i+=1
    return acumulador