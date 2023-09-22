def repetidos(lista):
    '''Recebe uma lista de número e retorna a quantidade de vezes
    que um número da lista é igual ao número nterior; list -> int'''
    i  = 0
    a = []
    while i < len(lista):
        if lista[i] == lista[i + 1]:
            a = a + 1
        i = i + 1
    return lan(a)