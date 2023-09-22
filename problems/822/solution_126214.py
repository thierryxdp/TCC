def repetidos(numeros):
    '''recebe uma lista de números e retorna o número 
    de vezes que um elemento da lista é igual ao elemento 
    anterior; list -> int'''
    
    i = 0
    j = 1
    numeros = []
   	    
    while len(numeros) < i:
        if numeros[i] == numeros[j]:
            x= numeros.count(i) 
                
    i = i+1
    j = j+1
  
	return x