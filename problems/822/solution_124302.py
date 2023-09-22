def repetidos(lista):
    """ funcao que recebe uma lista e retorna o numero de vezes que um numero
    e igual ao elemento interior. list->int"""
    proximo=0
    n=0
    while proximo<len(lista)-1:
        if lista[proximo]==lista[proximo+1]:
            n=n+1
        proximo= proximo+1
    return n