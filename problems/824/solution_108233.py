def uppCons (frase):
    """" """
    i=0
    consoantes="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    vogal="AÃÁÂEÉÊIÍOÔÓUÚaãáâeéêiíoôóuú"
    while frase[i] in consoantes:
        if frase[i] in "AÃÁÂEÉÊIÍOÔÓUÚaãáâeéêiíoôóuú":
            i=i+1
            frase= vogal
        else:
            frase=consoantes.upper()
            i=i+1
    return frase