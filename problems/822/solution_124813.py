def repetidos(lista):
    '''Função que recebe uma lista de números e retorna o número de vezes em que um elemento da lista foi igual ao anterior.
list --> int'''
    i = 0
    qtd_repeticoes = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            qtd_repeticoes = qtd_repeticoes + 1
        i = i+1
    return qtd_repeticoes