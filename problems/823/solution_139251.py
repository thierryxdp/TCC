def faltante (lista):
    '''Retorna qual inteiro está faltando numa lista de 1 a N inteiros, lista ->int'''
    inteiro = 1
    while inteiro in lista:
        inteiro = inteiro + 1
    return inteiro