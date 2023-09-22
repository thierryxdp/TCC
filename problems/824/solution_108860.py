def uppCons(frase):
    '''descricao'''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            i=i+1
            frase[i]=str.upper(frase[i])            
	final=str.join(' ', frase[i])
    return final