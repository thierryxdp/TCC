def uppCons(frase):
    """ Converte consoantes de uma frase em maiuscula
    str->str """
    
    frase_alt = ''
    for c in frase:
        if(c in 'bcçdfghjklmnpqrstvxwyz'):
            frase_alt += str.upper(c)
        else:
            frase_alt += c
    return frase_alt