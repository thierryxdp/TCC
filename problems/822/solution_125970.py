def repetidos(lista):
    '''função responsável por dizer quantas vezes ocorre a repetição de um termo de uma lista,lista'''
    i = 1
    repeticoes = 0
    while i < len(lista):
        if lista[i] == lista[i - 1]:
            repeticoes = repeticoes + 1
        i = i + 1
    return repeticoes