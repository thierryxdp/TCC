def repetidos(lista):
    ''' Função que recebe uma lista e retorna a quantidade de vezes em que um item
dessa lista e igual ao item na posicao anterior.
list -> int
'''
    vezes = 0
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1]:
            vezes += 1
    return vezes