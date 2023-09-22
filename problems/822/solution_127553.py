def repetidos(lista):
    '''Faça uma função que retorne o número de vezes que um elemento da lista é igual ao elemento anterior, list -> int'''
    x = 0
    repeticao = []
    while x<len(lista):
        lista_numero = lista[x]
        if lista_numero == 0:
            lista_numero = str.count(lista[x])
            repeticao = repeticao + lista_numero
        x = x + 1
    return repeticao