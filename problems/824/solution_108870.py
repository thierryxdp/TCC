def uppCons(frase):
    '''descricao'''
    i=0
    texto=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            texto=frase[:i]+str.upper(frase[i])+frase[i+1:]
        i=i+1
    return texto