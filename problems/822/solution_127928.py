def repetidos(x):
    '''
    Função que dada uma lista de números, retorna o número de vezes que um elemento
    da lista é igual ao elemento anterior
    list-> int
    '''
    pares = 1
    i = 0
    while i<len(x):
        i = i + 1
        if x[i] == x[i+1]:
        pares = pares + i
        return pares