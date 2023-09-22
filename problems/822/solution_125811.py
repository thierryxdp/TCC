def repetidos(lista):
    '''funcao que retorna o numero de vezes em que há 2 elementos seguidos
    com um mesmo valor na respectiva lista de entrada
    list(int) -> int'''
    repeticao = 0
    indice = 0
    while indice < len(lista):
        if lista[indice] == lista[indice+1]:
            repeticao = repeticao + 1
        indice = indice + 1
    return repeticao