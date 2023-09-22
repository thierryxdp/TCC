def repetidos (lista_numeros):
    '''função que dada uma lista de números, retorne o número
    de vezes que um elemento da lista é igual ao anterior
    list -> int'''
    i = 0
    repetidos =  0

    while i < len(lista_numeros) - 1:
        if lista_numeros[i] == lista_numeros[i+1]:
            repetidos += 1
        i += 1
    return repetidos