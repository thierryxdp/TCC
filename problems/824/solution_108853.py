def uppCons(frase):
    frase1=''.join(frase)
    a=''
    for caractere in frase1:
        if caractere in 'BCDFGHJKLMNPQRSTVXYZÇbcdfghjklmnpqrstvxyzç':
            a+= caractere.upper()
        else:
            a+=caractere
    return a