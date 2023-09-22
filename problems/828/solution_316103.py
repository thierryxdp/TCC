def primo(num):

    '''
    funcao que recebe um numero e retorna se ele é ou nao primo
    int -> bool
    '''
    i =  1
    divisor = 0    
    for i in range(1,num+1):
        if num%i == 0:
            divisor += 1
    i += 1
    	if divisor == 2:
        	return True 
    	else:
        	return False