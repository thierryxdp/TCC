def repetidos(numeros):
    '''retorna o número de vezes que um elemento da lista(numeros) é igual
    ao elemento anterior a ele;
    list -> int'''
    i=0
    num_repetidos=0
    while i < len(numeros):
        if numeros[i]==numeros[i-1]:
            num_repetidos = num_repetidos + 1
        i=i+1
    return num_repetidos