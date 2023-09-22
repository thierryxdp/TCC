def repetidos(numeros):
    """Recebe uma lista de números e retorna o número de vezes em que um
elemento da lista é igual ao seu antecessor;
str -> int"""
    proximo = 1
    acumulador = 0

    while proximo < len(numeros):
        if numeros[proximo] == numeros[proximo-1]:
            acumulador = acumulador + 1
        proximo = proximo + 1
        
    return acumulador