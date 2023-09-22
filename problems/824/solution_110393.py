def uppCons(frase):
    Nfrase = ()
    i=0
    consu='BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz'

    while i<len(frase):
        if frase[i] in consu:
            x = str.upper(frase[i])
            Nfrase[i]=x
        else:
            Nfrase=frase[i]
        i=i+1

    Junta=" ".join(Nfrase)
    return Junta