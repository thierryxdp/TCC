def primo(n):
    '''Dado um númro inteiro n retorna se n é primo.
    int -> int'''
    acumul = 0
    cont = 1
    if n == 2:
        return True
    else:   
    	while cont <= n:
        	if n%cont == 0:
            	acumul += 1
        	cont += 2
    	return acumul == 2