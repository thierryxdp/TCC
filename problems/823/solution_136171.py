def faltante(lista):
    '''
    	Dado uma lista, descobre qual número inteiro deste intervalo que est[ faltando.
        list -> int
	'''
    
	i=0
    result = 0
    while (i<len(lista)):
        ant = i-1
        if (lista[0]==2):
            result=1
            break
        elif (lista[i]-lista[ant]!=1):
            result = lista[i]-1
        else:
            result = lista[len(lista)]+1
        i+=1
    return result