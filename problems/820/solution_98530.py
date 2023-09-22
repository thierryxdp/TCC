def posLetra (frase, letra, num):
    '''Recebe uma frase e procura em que pósição está a letra no ocorência dada pelo usuário.
    str, str, int -> int'''
    i = 0
    c = 0
    posicao = 0
    while c < num:
        posicao = str.index(frase, letra, c)
        c = c + 1
    return posicao

		if frase[c] in letra:
        else:
            posicao = -1