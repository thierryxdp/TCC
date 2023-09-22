def uppCons(frase):
    Nfrase = frase.split()
    i=0

    while i<len(frase):
        if Nfrase[i] in 'BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz':
            Up = str.upper(Nfrase)
            Nfrase[i] = Up
        i=i+1

    Junta=" ".join(Nfrase)
    return Junta