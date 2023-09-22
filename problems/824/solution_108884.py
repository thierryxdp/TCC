def uppCons(frase):
    '''descricao'''
    i=0
    i=i+1
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            texto=texto+str.upper(frase[i])
    return frase