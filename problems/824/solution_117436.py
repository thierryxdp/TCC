def uppCons(frase):
    '''descrição'''
    i = 0
    l_frase = frase.split()
    
    while i < len(l_frase):
        while 'aeiou' not in frase:
            return frase[i]
        i += 1