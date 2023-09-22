def repetidos(lista):
    '''Recebe como entrada uma lista de números e retorna a quantidade de vezes
que um elemento da lista é igual ao elemento anterior.'''
    n = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo] == lista[proximo]:
            n = n + (lista[proximo],)

        proximo = proximo + 1

        return len(n)