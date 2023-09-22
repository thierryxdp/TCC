def faltante(lista):
    '''
    	Dado uma lista, descobre qual número inteiro deste intervalo que est[ faltando.
        list -> int
	'''
    
	i=0
    result = 0
    while (i<len(lista)):
        ant = i-1
        if (len(lista)==1) and lista[i]==1:
            result = 2
            break
        if (lista[0]==2):
            result=1
            break
        if ((lista[i]-lista[ant])!=1):
            result = lista[ant]
            
        else:
            result = len(lista)+1
        i+=1
    return result