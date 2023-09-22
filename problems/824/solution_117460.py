def uppCons(frase):
    '''descrição'''
    i = 0
    tot = 0
    l_frase = frase.split()
    vogais = 'a','e','i','u','A','E','I','O','U'
    while i < len(l_frase):
        if i not in list(frase):
            return frase
        i += 1