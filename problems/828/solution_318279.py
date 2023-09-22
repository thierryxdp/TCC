def primo (numero):
    '''Diz se um número é primo, int-> valor booleano'''
    for menores in range(numero):
        if numero%menores=0:
            return False
        else:
            return True