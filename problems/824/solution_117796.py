def uppCons(frase):
    ''' '''
    indice=0    
    while indice < len(frase):
        if frase[indice] in 'BCDFGHJKLMNPQRSTUVWXYZbcdfghjklmnpqrstvwxyz':
            maiuscula=frase[indice].upper()
        frase_nova=frase.replace(frase[indice],maiscula)
        indice+=1
    return frase_nova