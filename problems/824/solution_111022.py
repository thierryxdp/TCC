def uppCons(x):
    '''Retona a frase com as consoantes em maiúsculo.
    str -> str'''
    s = ''
    for caractere in x:
        if caractere in 'bcdfghjklmnpqrstvxwyzç':
            s += caractere.upper()
        else:
            s += caractere
    return s