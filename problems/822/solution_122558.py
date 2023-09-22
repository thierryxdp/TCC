def repetidos(lista):
    '''Função que recebe uma lista de números inteiros e retorna o número de vezes que
    um elemento da lista é igual ao elemento anterior, list -> int'''
    cont = 1
    result = 0
    while cont < len(lista):
        if lista[cont] == lista[cont-1]:
            result += 1

        cont += 1

    return result