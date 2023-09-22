def uppCons(frase):
    i=0
    consoante= ''
    while i<len(frase):
        if frase[i] in 'BCDFGHJKLMNPQRSTUVWXYZbcdfghjklmnpqrstvwxyz':
            consoante=frase[i]
            i=i+1
            return consoante