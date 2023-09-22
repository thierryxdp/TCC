def uppCons(string): 
    '''Recebe uma frase e a retorna, mas com todas as consoantes em maiúsculo;
    str -> str'''

    frase = ''
    i = 0
    consoantes = 'bcdfghjklmnpqrstvwxyzç'

    while i < len(string):
        if string[i] in consoantes:
            frase = frase + string[i].upper()
        else:
            frase = frase + string[i]
        i = i+1
    return frase