def consoantes(c):
    return letra.lower() in 'bcdfghjklmnpqrtvwxyzç'
def uppCons(frase):
    ''' str -> str'''
    nova_frase = ''
    i = 0
    while i < len(frase):
        letra = frase[i]
        
        if consoantes(c):
            c = str.upper(c)
        nova_frase += letra
        i += 1
    return nova_frase