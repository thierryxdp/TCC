def primo (numero):
    '''Diz se um número é primo, int-> valor booleano'''
    menores = numero - 1
    for menores != 1:
        if numero%menores==0:
            return False
        menores = menores - 1
        else:
            return True