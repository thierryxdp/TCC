def uppCons (frase):
    ''' '''
    i=0
    while i < len(frase):
        if frase[i] in 'bçcdfghjklmnpqrstvxwyz':
            subir= str.upper (frase[i])
            rep= str.replace(frase,frase[i],subir)
            frase= rep
        i=i+1
    return frase