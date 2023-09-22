def faltante(lista):
    '''Entre com uma lista para ser retornado o valor que esta faltando
    Lista -> Int'''
	i=1
    tam=(len(lista))+1
    num=0
    
    while i<tam:
        if lista[i-1]!=i:
            num=i
            return num
        i=i+1
        
    if num==0:
        return lista[-1]+1
    else:
    	return lista[0]+1