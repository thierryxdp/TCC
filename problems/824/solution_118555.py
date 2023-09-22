def uppCons(frase):
    consoante=''
    i = 0
    while i < len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvxyz':
            consoante = str.replace(frase,frase[i],str.upper(frase[i]))
        i = i + 1
    return consoante