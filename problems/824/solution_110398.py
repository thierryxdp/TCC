def uppCons(frase):
    Nfrase = ()
    i=0
    consu='BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz'

    while i<len(frase):
        if frase[i] in consu:
            Nfrase=Nfrase+(str.upper(frase[i],))
        else:
            Nfrase=Nfrase+(frase[i],)
        i=i+1

    Junta=" ".join(Nfrase)
    return Junta