def substitui (s, x, i):
    '''Retorna a string "s" inserida porém com o elemento da posição definida por "i" sendo substituído pelo caractere "x";
    str, str, int -> str'''
    frase = s
    return frase.replace(frase[i], x)