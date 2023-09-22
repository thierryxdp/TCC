def repetidos(lista):
    '''Função que recebe uma lista de números como entrada e retorna o numero de vezes que um elemento da lista é repetido.
    list -> int'''
    repeticao = 0
    proximo = 0
    while proximo < len(lista):
        if lista[proximo + 1] == lista[proximo]:
            repeticao = repeticao + 1
        proximo = proximo + 1
    return repeticao