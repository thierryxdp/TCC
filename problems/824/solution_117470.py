def uppCons(frase):
    '''Recebe uma frase e retorna a frase com as consoantes
    em maisculas.
    string -> string'''
    i = 0
    tot = 0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
    return frase[i].upper()
        i += 1