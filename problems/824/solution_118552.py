def uppCons(frase):
    consoante=''
    i = 0
    while i < len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvxyz':
            consoante = consoante + str.upper(frase[i]) in frase
        i = i + 1
    return consoante