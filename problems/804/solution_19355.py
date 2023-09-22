def filtra_pares (tupla):
    '''
    	Funcao que recebe uma tupla com quatro elementos inteiros
        como parametros e retorna uma nova tupla contendo apenas os 
        elementos pares da tupla original, na mesma ordem em que se
        encontravam.
        Parametros: (tupla) tuple.
        Return: tuple.
	'''
    
    tupla = num1,num2,num3,num4
    pares = tuple()
    
    if (num1%2 == 0):
        pares += (num1,)
        
	if (num2%2 == 0):
        pares += (num2,)
        
	if (num3%2 == 0):
        pares += (num3,)
        
	if (num4%2 == 0):
        pares += (num4,)
        
	return pares