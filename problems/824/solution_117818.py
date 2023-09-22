def uppCons(frase):
    ''' '''
    indice=0    
    while indice < len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
             str.upper(frase[indice])
        	frase_nova= frase.replace(frase[indice],maiuscula)
        indice+=1
    return frase_nova