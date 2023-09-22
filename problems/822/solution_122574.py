def repetidos(lista):
    '''Função que recebe uma lista números inteiros e retorna o número de
    vezes em que houveram repetições de números na lista. list -> int'''
    i = 0
    acumulador = [] 
    x = 0 
    while i <= len(lista):
        if lista[i] == lista[i-1]:
            acumulador = acumulador + [lista[i],]
            x = len(acumulador)
        i = i + 1
    return x