def primo (numero):
    '''Diz se um número é primo, int-> valor booleano'''
    reducao = numero/2
    while elemento in range(reducao):
        if numero%reducao==0 and elemento!=1:
            return False
        else:
            return True