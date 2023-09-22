def primo (numero):
    '''Diz se um número é primo, int-> valor booleano'''
    for elemento in range(numero):
        if numero%elemento!=0:
            return False
        else:
            return True