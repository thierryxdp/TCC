def primo(x):
    '''Funcão que recebe um int x e retorna um booleano verificando se x é
    primo ou não'''
    from sympy import isprime
    if (isprime(int(x)))== True:
        return True
	else:
       
        return False