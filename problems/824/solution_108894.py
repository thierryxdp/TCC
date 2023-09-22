def uppCons(frase):
    '''descricao'''
    i=0
    texto=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            i=i+1
            texto=frase[:i]+str.upper(frase[i])+frase[i:]  
    return texto