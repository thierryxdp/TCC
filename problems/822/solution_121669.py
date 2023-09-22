# Repetidos
def repetidos(lista):
    '''Dada uma lista de números a função deve retornar o número
    de vezes em que um elemento é igual ao seu antecessor;
    LIST -> INT'''
    i = 0
    repeat = 0
    while i in range(0, len(lista)):
        if(lista[i] == lista[(i-1)]):
            repeat += 1
        i += 1
    return repeat