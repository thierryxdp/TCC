def repetidos(lista):
    '''função que recebe uma lista de números e retorna o número de vezes que um elemento 
    é igual ao seu anterior
    lista -> int'''
    y = 0
    proximo = 0
    x = 1
    while proximo < len(lista) and x < len(lista):
        if lista[proximo] == lista[x]:
            y = y + 1
        proximo = proximo + 1
        x = x + 1
    return y