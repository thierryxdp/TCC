def repetidos(numeros):
    '''dado uma lista, a funcao retornara o numero de vezes que um numero foi igual ao seu antecessor'''
    valor = 0
    i = 1
    while i<len(numeros):
        if numeros[i] == numeros[i-1]:
            valor = valor + 1
        i+ = 1
    return valor