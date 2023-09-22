def uppCons(frase):
    i=''
    for caractere in frase:
        if caractere in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            i += caractere.upper()
        else:
            i+= caractere
            return i