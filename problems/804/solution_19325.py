def filtra_pares (tupla):
    '''
    	Funcao que recebe uma tupla com quatro elementos inteiros
        como parametros e retorna uma nova tupla contendo apenas os 
        elementos pares da tupla original, na mesma ordem em que se
        encontravam.
        Parametros: (tupla) tuple.
        Return: tuple.
	'''
    tupla = (num1,)(num2,)(num3,)(num4,)
    pares = tuple()
    
    	if (tupla[0]%2 == 0):
        	pares = tuple() + (num1,)
        
		elif ((num2,)%2 == 0):
        	pares = tuple() + (num2,)
        
		elif ((num3,)%2 == 0):
        	pares = tuple() + (num3,)
        
		elif ((num4,)%2 == 0):
        	pares = tuple() + (num4,)
        
		return pares