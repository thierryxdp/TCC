def repetidos(lista):
    '''Funçao que retorna o numero de vezes que dois 
    elementos consecutivos da lista são iguais.
    list -> int'''
    
    x=0
    repetidos=0
    
	while x+1<len(lista):
    	if lista[x]==lista[x+1]:
      	x=x+1
        repetidos=repetidos+1