def uppCons(frase):
    Nfrase = frase.split()
    i=0
    consu='BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz'

    while i<len(frase):
        if frase[i] in consu:
            Nfrase=Nfrase+(frase.upper())
        else:
            Nfrase=Nfrase+(frase[i],)
        i=i+1

    Junta=" ".join(Nfrase)
    return Nfrase