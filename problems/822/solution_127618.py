def repetidos(numeros):
    '''retorna o numero de vezes que um elemento da lista é igual ao anterior
    int -> int'''
    i=0
    repetidos=0
    while i<len(numeros):
        if numeros[i]==numeros[i-1]:
            repetidos=repetidos + 1
        i=i+1
    return repetidos