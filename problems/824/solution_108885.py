def uppCons(frase):
    '''descricao'''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            texto=texto+str.upper(frase[i])
            i=i+1
    return frase