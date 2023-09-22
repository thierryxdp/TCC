def repetidos(lista):
    '''funcao que retorna o numero de vezes que um elemento da lista é igual ao anterior'''
    repeticao = 0
    i = 0
    for i in range (len(lista)-1):
        if lista[i] == (lista[i+1]):
            repeticao = repeticao + 1
        i = i + 1
    return repeticao