def repetidos(lista):
    '''
    funcao que recebe uma lista de numeros de entrada e
    retorna o numero de vezes que um elemento
    da lista é igual ao elemento anterior
    list->int
    '''
    x=0
    y=0
    z=0
    while x<len(lista):
        if lista[y]==lista[y-1]:
            z=z+1
        y=y+1
        x=x+1

    return z