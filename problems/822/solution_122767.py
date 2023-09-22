def repetidos(lista):
    '''função que dada uma lista de números, retorna a quantidade de vezes 
       em que um elemento é igual ao elemento anterior. list -> int'''
    pos = 1
    acumulador = 0
    while (pos < len(lista)):
        if (lisa[pos] == lista[pos - 1]):
            acumulador = acumulador + 1
        pos = pos + 1
    return acumulador