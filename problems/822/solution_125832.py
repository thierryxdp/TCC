def repetidos(lista):
    '''funcao que retorna o numero de vezes em que há 2 elementos seguidos
    com um mesmo valor na respectiva lista de entrada
    list(int) -> int'''
    repeticao = 0
    i = 0
    while i < len(lista):
        if lista[i]==lista[i+1]:
            repeticao = repeticao + 1
        i = i + 1
    return repeticao