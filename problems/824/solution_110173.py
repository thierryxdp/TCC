def uppCons (frase):
    '''função que recebe uma frase e retorne essa mesma frase
    com todas as consoantes em maiúsculas.
    string -> string'''
    fraseF = ''
    proximo = 0
    
    while proximo < len(frase):
        if 'bcdfghjklmnpqrstvwxyz' in frase:
            fraseF = fraseF + str.upper(len[proximo])
        return fraseF