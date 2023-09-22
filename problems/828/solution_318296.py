def primo (numero):
    '''Diz se um número é primo, int-> valor booleano'''
    elemento = 2
    for elemento in range(numero) and elemento not in [0, 1]:
        if numero%elemento!=0:
            return False
        else:
            return True