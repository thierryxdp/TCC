def uppCons(frase):
    i = 0
    while i < len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvxyz':
        i = i + 1
    return str.replace(frase,frase[i],str.upper(frase[i]))