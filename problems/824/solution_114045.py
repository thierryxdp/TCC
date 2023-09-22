def uppCons(frase):
    i = 0
    nobaFrase = ''
    
    while i<len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            frase.upper(frase[i])
        i = i + 1
        
    return nobaFrase