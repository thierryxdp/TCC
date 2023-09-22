def repetidos(lista):
    '''ao receber uma lista de números inteiros,
    retorna a quantidade de vezes que um elemento
    é igual ao elemento diretamente anterior a ele.
    list -> int'''
    n = 0
    vezes = []
    while n < len(lista):
        if lista[n] == lista[n-1] and n > 0:
            vezes.append(lista[n])
        n = n + 1
    return len(vezes)