def consoantes(letra):
    return letra.lower() in 'bcdfghjklmnpqrtvwxyzç'

def uppCons(frase):
    '''str->str'''
    nova_frase = ''
    i = 0
    while i < len(frase):
        letra = frase[i]
        if consoantes(letra):
            letra = str.upper(letra)
        nova_frase += letra
        i += 1
        return nova_frase