def uppCons (frase):
    '''função que recebe como entrada uma frase e rotorna essa
    frase com todas as consoantes MAIÚSCULAS, e o resto da fra
    se original, str->str'''
    consoante=0
    while consoante<len(frase):
        if frase[consoante] in 'bcdfghjklmnpqrstvwyxz':
            str.upper(frase[consoante])
    	consoante+=1
    return frase