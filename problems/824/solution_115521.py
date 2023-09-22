def uppCons(frase):
    
    if frase() in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
        frase.replace(frase(),str.upper(frase))
        
        return frase