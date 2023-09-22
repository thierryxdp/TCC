def consoantes(c):
    return c.lower() in 'bcdfghjklmnpqrstvwxyzç'
def uppCons(frase):
    ''' str -> str'''
    nova_frase = ''
    i = 0
    while i < len(frase):
        c = frase[i]
        if consoantes(c):
            c = str.upper(c)
        nova_frase += c
        i += 1
    return nova_frase