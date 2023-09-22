def posLetra (frase, letra, num):
    '''Recebe uma frase e procura em que pósição está a letra no ocorência dada pelo usuário.
    str, str, int -> int'''
    i = 0
    c = 0
    posicao = 0
    while i < num:
        if frase[c] = letra:
            posicao = str.index(frase, letra, i)
            i = i+1
        else:
            posicao = -1
        c = c + 1
    return posicao