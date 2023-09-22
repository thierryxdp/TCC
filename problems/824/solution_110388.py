def uppCons(frase):
    Nfrase = frase.split()
    i=0
    consu='BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz'

    while i<len(frase):
        if Nfrase[i] in consu:
            Nfrase=str.upper(Nfrase[i])
        i=i+1

    Junta=" ".join(Nfrase)
    return Junta