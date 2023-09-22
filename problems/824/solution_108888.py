def uppCons(frase):
    '''descricao'''
    i=0
    texto=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            texto=texto[:i]+str.upper(frase[i])+texto[i:]
        i=i+1
    return frase