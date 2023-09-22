def substitui(s, x, i):
    """ 
    s: string 
    x: caractere
    i: numero inteiro
    return: string igual a s, exceto que o elemento
    da posicao i deve ser subst pelo caractere x
    """
    return s[0:i] + x + s[i + 1:]