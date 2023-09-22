def repetidos(numeros):
    '''retorna a quantidade de números repetidos em uma lista;
    list -> int'''
    
    numeros = []
    i = 0
    qtd = 0
    
    while i < len(numeros):
        if item in numeros:
            item = numeros[i] 
            qtd = len( set( [ item for item in lista if lista.count( item ) > 1] ) )
        
                
    i = i + 1 
              
	return qtd