def filtra_pares (a, b, c, d):
    '''funcao ira receber quatro entradas, e avaliar 
    se estas sao pares ou impares, e 
    retornar em uma lista aquelas entradas que sao pares
    int, int, int, int --> [int, int, int, int]'''
    lista = []
    if (a % 2 == 0) == True:
        lista.append (a)
    if (b % 2 == 0) == True:
        lista.append (b)
    if (c % 2 == 0) == True:
        lista.append (c)
    if (d % 2 == 0) == True:
        lista.append (d)
    return lista