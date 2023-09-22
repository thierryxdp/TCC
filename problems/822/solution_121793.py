def repetidos(lista):
    """função que receba uma lista e retorne o número de vezes que um elemento da lista é igual ao anterior;
    list -> int"""
    acumulador = 0
    proximo = 1
    while proximo< len(lista):
        if lista[proximo] == lista[proximo - 1]:
            acumulador = acumulador + 1
        proximo = proximo + 1
    return acumulador