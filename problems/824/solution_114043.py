def uppCons(frase):
    i = 0
    nobaFrase = ''
    
    while i<len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            nobaFrase =  nobaFrase + frase[i]
        i = i + 1
        
    return nobafrase.upper()