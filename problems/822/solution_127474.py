def repetidos(numeros):
    '''Retorna a quantidade de vezes que um elemento é igual ao
    anterior;
    [int]->int'''
    
    repeticoes=0
    i=0
    
    while i<len(numeros):
        if numeros[i]==numeros[i-1]:
        	repeticoes+=1
        i+=1
    return repeticoes