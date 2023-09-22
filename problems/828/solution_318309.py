def primo (numero):
    '''Diz se um número é primo, int-> valor booleano'''
    proximo = 1
    usados=[]
    divisores = []
    while proximo in range(numero):
        if numero%(proximo)==0 and len(divisores)<2:
            divisores = divisores + [proximo]
    	proximo = proximo + 2
    if len(divisores)==1:
        return True
    else:
        return False