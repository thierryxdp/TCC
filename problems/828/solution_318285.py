def primo (numero):
    '''Diz se um número é primo, int-> valor booleano'''
    for elemento in range(numero) and elemento not in [0]:
        if numero%elemento==0 and elemento!=1:
            return False
        else:
            return True