def repetidos(lista):
    """"Esta função recebe uma lista e retorna a quantidade de vezes em que um elemento da lista é igual ao anterior.
    list -> int"""
    posicao = 1
    acumulador = 0
    for i in lista:
        if lista[posicao] == lista[posicao-1]:
            acumulador += 1
    return acumulador