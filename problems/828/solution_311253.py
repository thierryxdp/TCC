def primo(n):
    '''dado um número n positivo, retorna se este número é primo ou não.
    int ->bool'''
    divisores =0
    primo =True
    for i in range(3,n):
        if n%i ==0:
            divisores +=1
        	if divisores ==0:
            	return primo
        	else:
            	return not primo