def uppCons(frase):
    '''descricao'''
    i=0
    texto=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz': 
            texto=frase+str.upper(frase[i])
        else:
            texto=str(frase[i])
    return texto