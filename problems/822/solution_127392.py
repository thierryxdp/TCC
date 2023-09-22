def repetidos(numeros):
    '''recebe e retorna o número de vezes que há uma sequência de números iguais
    	list -> int'''
    
    i=0
    j=0
    
    while j<len(numeros):
        i=i+1
        if numeros[i-1]==numeros[i]:
            
            j=j+1
    return j