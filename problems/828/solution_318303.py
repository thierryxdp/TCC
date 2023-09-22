def primo (numero):
    '''Diz se um número é primo, int-> valor booleano'''
    proximo = 2
    divisores = [1]
    while proximo in range(numero//2):
        if numero%(proximo)==0:
            divisores = divisores + [proximo]
    	proximo = proximo + 1
    if len(divisores)==1:
        return True
    else:
        return False