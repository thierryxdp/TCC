def uppCons(frase):
    i = 0
    frase1 = ''
    
    while i<len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            frase.upper()
            frase1 = frase
        else:
            frase[i].lower()
        frase1 = frase
        i = i + 1
        
    return frase1