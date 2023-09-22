def primo (numero):
    '''Diz se um número é primo, int-> valor booleano'''
    proximo = 3
    divisores = [1]
    while proximo in range(numero):
        if numero%(proximo - 1)==0:
            divisores = divisores + [proximo]
    	proximo = proximo + 1
    if len(divisores)==0:
        return True
    else:
        return False