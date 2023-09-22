def primo (n):
    '''função que dada um numero inteiro positivo diz se ele é primo; int ->bool'''
    for divisor in (n,n+1):
        if n!=divisor and divisor!=1 and n%divisor==0:
        	return True
        else:
            return False