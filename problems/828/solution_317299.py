def primo (n):
    '''função que dada um numero inteiro positivo diz se ele é primo; int ->bool'''
    for divisor in range(n,n+1):
        if n%divisor==0:
        	return False
        else:
            return True