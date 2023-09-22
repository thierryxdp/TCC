def repetidos(numeros):
    '''recebe uma lista de números e retorna o número 
    de vezes que um elemento da lista é igual ao elemento 
    anterior; list -> int'''
    
    i = 0
    j = 1
   	numeros = []
    
    while i  < len(numeros):
        if numeros[i] == numeros[j]:
                x = 1  
    i = i+1
    j = j+1
  
	return x