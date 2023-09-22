def repetidos(lista):
    ''' função que receba como entrada uma lista de números, e retorne o número de vezes que um elemento da lista é igual ao elemento anterior.
    Entrada: list;
    Saída: int'''
    acumulador = 0
    proximo = 1
    while próximo < len(lista):
        if lista(próximo) == lista(próximo - 1):
            acumulador = acumulador + 1
        próximo = próximo + 1
    return acumulador