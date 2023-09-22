def repetidos(lista):
    '''funcao que dado uma lista, retorna o numero de vezes em que um numero foi igual ao seu antecessor
    list->int'''
    x=1
    n=0
    while x<len(lista):
        if lista[x]==lista[x-1]:
            n=n+1
        else:
            n
        x=x+1
    return n