def uppCons(frase):
    i = 0
    frase1 = ''
    
    while i<len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            frase[i].upper()
        frase1 = frase
        i = i + 1
        
    return frase1