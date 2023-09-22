def uppCons(frase):
    consoante=''
    i = 0
    while i < len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvxyz':
            consoante =consoante + frase
        i = i + 1
    return consoante