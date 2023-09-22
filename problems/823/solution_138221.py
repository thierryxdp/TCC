def faltante(numeros):

    i = 0
    n = 1
    
    if numeros[0] != 1: # ver se o 1 está faltando
        return 1
    while i < len(numeros):
        if numeros[i] in '123456789':
            i += 1
        if numeros [i] not in '123456789':

            return i + 1