def uppCons(frase):
    '''descricao'''
    i=0
    texto=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz': 
            texto=frase+str.upper(frase[i])
            i=i+1
        else:
            texto=str(frase[i])
        	i=i+1
    return texto