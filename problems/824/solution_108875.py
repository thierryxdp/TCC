def uppCons(frase):
    '''descricao'''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frase[0,i]=str.upper(frase[i])
        i=i+1
    return frase