def uppCons(frase):
    '''descricao'''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frase[i,0]=str.upper(frase[i])
        i=i+1
    return frase