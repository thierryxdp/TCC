def repetidos(lista):
    '''A funcao recebe uma lista de numeros e retorna o numero de vezes em que um numero
e igual a seu antecessor list->int'''
    n=[]
    ordem=0
    while ordem<len(lista):
        if lista[ordem]==lista[ordem-1]:
            n.append('.')
        ordem=ordem+1
    return len(n)