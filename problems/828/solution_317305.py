def primo (n):
    '''função que dada um numero inteiro positivo diz se ele é primo; int ->bool'''
    for divisor in range(1,n+1):
        if n%divisor==0:
        	return False
        elif divisor!=n and divisor!=1 and n%divisor!=0:
            return True