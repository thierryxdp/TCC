def repetidos(lista):
    '''Função que receba uma lista de números, e retorne o número de vezes ocorre uma série de números iguais'''
    '''list -> int'''
    quantas_vezes = 0
    i = 1
    while i < len(lista):
        if lista[i] == lista[i-1]:
            lista.count(lista[i])
            quantas_vezes = quantas_vezes + 1
        i= i + 1
    return quantas_vezes