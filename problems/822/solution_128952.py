def repetidos(lista):
    '''retorna o número de vezes que um elemento da lista
    é igual ao elemento anterior'''

    n = len(lista) -1
    qtd = 0
    
    while n > 0:

        if lista[n] == lista[n-1]:
            qtd = qtd + 1
        n = n-1

    return qtd