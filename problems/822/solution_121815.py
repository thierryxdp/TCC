def repetidos(lista):
    '''Retorna o número de vezes que um elemento da lista é igual ao elemento anterior;
    list -> int'''
    i = 0
    qtd = 0
    while i< len(lista):
        if lista[i-1] == lista[i]:
            qtd = qtd + 1

        i = i+1

    return qtd