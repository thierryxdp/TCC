def filtra_pares (tupla):
    '''
    	Funcao que recebe uma tupla com quatro elementos inteiros
        como parametros e retorna uma nova tupla contendo apenas os 
        elementos pares da tupla original, na mesma ordem em que se
        encontravam.
        Parametros: (tupla) tuple.
        Return: tuple.
	'''
    tupla = (num1,num2,num3,num4)
    pares = tuple()
    
    if (type(tupla) == tuple) and (len(tupla) == 4) and (type(tupla) == int):
    
    	if (tupla[0]%2 == 0):
        	pares = tuple() + (num1,)
        
		elif (tupla[1]%2 == 0):
        	pares = tuple() + (num2,)
        
		elif (tupla[2]%2 == 0):
        	pares = tuple() + (num3,)
        
		elif (tupla[3]%2 == 0):
        	pares = tuple() + (num4,)
        
			return pares