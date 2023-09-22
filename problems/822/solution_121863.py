def repetidos(lista):
    '''funcão que recebe como entrada uma lista de números, e retorna o número
    de vezes que um elemento da lista é igual ao elemento anterior. lista -> int'''
    i = 1
    repeticao = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            repeticao = repeticao + 1
        i = i + 1
    return repeticao