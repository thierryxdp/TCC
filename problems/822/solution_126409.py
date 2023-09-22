def repetidos(lista):
    '''Dado uma lista de números inteiros, retornará o npumero de
    vezes que um elemento da lista é igual ao elemento anterior.(lista=>lista)'''

    repeticao = 0
    i = 0
    j = 1

    while j < len(lista):
        if lista[j] == lista[i]:
            repeticao = repeticao + 1
        i = i + 1
        j = j + 1
    return repeticao