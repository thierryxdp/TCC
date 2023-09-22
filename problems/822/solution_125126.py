def repetidos(lista):
    '''retorna o número de vezes que um elemento n da lista é
    igual ao elemento n - 1 da lista; list -> int'''
    i = 0
    acumulador = 0
    while i < len(lista):
        if lista[i] == lista[i - 1]:
            acumulador = acumulador + 1
        i = i + 1
    return acumulador