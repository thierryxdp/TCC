def uppCons(frase):
    '''Retorne a frase com todas as suas
    consoantes em maiusculas.
    str -> str'''
    i = 0
    consoante = ''
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyzç':
            consoante = consoante + str.upper(frase[i])
        else:
            consoante = consoante + frase[i]
        i = i + 1
    return consoante