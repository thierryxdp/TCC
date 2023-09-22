def repetidos(numeros):
    '''recebe uma lista de números, e retorna a quantidade de vezes
    onde ele é igual ao elemento anterior'''
    i=0
    d=0
    while i < len( numeros):
        if numeros[i]==numeros[i-1]:
            d=d+1
        i=i+1
    return d