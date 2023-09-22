def repetidos(lista):
    '''Função que recebe uma lista e retorna o número de vezes que um elemento da lista é igual ao elemento anterior
    list -> int'''
    n = 0
    v = 0
    c = (n+1)
    while n<((len(lista))-1):
        if lista[n] == lista[c]:
            v= v+1
        n= n+1
        c=(n+1)
    return v