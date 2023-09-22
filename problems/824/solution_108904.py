def uppCons(frase):
    '''descricao'''
    i=0
    texto=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç': 
            texto=texto+str.upper(frase[i])
            i=i+1
        else:
            texto=texto+str(frase[i])
        	i=i+1
    return texto