def repetidos(lista):
    '''Dado uma lista de números, retorna o número de vezes 
    que um elemento da lista é igual ao anterior.
    list --> int'''
    a = len(lista)
    b = 0
    c = 0
    proximo = 0
    while proximo < a:
        if lista[b] == lista[b+1]:
            c = c+1
        proximo = proximo + 1
    return c