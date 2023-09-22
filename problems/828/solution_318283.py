def primo (numero):
    '''Diz se um número é primo, int-> valor booleano'''
    for elemento in range(numero):
        if numero%reducao==0 and elemento!=1:
            return False
        else:
            return True