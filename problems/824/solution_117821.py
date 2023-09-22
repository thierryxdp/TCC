def uppCons(frase):
    ''' '''
    indice=0
    frase_nova=''
    while indice < len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            maiuscula = str.upper(frase[indice])
        	frase_nova= frase_nova + frase.replace(frase[indice],maiuscula)
        indice+=1
    return frase_nova