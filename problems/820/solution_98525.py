def posLetra (frase, letra, num):
    '''Recebe uma frase e procura em que pósição está a letra no ocorência dada pelo usuário.
    str, str, int -> int'''
    i = 0
    c = 0
    posicao = -1
    while i < num:
        if frase[c] not in letra:
            posicao = -1
        else:
            posicao = str.index(frase, letra, c)
            i = i + 1
        c = c + 1
    return posicao