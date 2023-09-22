def uppCons (frase):
    '''função que recebe uma frase e retorne essa mesma frase
    com todas as consoantes em maiúsculas.
    string -> string'''
    proximo = 0
    
    while proximo < len(frase):
        if 'bcdfghjklmnpqrstvwxyz' in frase:
            frase = frase + str.upper(len[proximo])
    return frase