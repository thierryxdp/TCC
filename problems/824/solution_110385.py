def uppCons(frase):
    Nfrase = frase.split()
    i=0
    consu='BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz'

    while i<len(frase):
        if Nfrase[i] in consu:
            Up = str.upper(Nfrase)
            Nfrase[i]=Up
        i=i+1

    Junta=" ".join(Nfrase)
    return Junta