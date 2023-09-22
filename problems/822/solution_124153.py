def repetidos(lista):
    '''Funcao que retorna o numero de vezes que um elemento da lista
    e igual ao elemento anterior'''
    x=0
    y=0
    while x<len(lista):
        if lista[x]==lista[x-1]:
            y=y+1
        x=x+1
    return y