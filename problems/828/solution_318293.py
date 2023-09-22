def primo (numero):
    '''Diz se um número é primo, int-> valor booleano'''
    divisor = 2
    for divisor in range(numero//2):	
    	if numero%divisor!=0:
    		divisor = divisor + 1
    if divisor == 2:
        return True
    else:
        return False