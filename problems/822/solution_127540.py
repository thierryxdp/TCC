def repetidos(lista):
    '''Faça uma função que retorne o número de vezes que um elemento da lista é igual ao elemento anterior, list -> int'''
    x = 0
    repeticao = []
    while x<len(lista):
        if lista[x] == 0:
            repeticao.count(lista, x)
        x = x + 1
    return repeticao