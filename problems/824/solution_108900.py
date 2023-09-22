def uppCons(frase):
    '''descricao'''
    i=0
    texto=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            texto=frase[:i]+str.upper(frase[i])+frase[i:]
        else:
            texto=str(frase[:i]+frase[i]+frase[i:])
        i=i+1
    return texto