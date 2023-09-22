def repetidos(numeros):
    '''Retorna a quantidade de vezes que um elemento é igual ao
    anterior;
    [int]->int'''
    
    repeticoes=0
    i=0
    i_n=0
    
    while i<len(numeros):
        if i_n==numeros[i]:
        repeticoes+=1
        i+=1
        i_n+=-1
        
       
   	return repeticoes