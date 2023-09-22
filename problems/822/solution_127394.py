def repetidos(numeros):
    '''recebe e retorna o número de vezes que há uma sequência de números iguais
    	list -> int'''
    
    i=1
    j=0
    
    while i<len(numeros):
        
        if numeros[i-1]==numeros[i]:
            
            j=j+1
    i=i+1
    
    return j