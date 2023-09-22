def uppCons (frase):
    """" """
    i=0
    string= ""
    consoantes="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    vogal="AÃÁÂEÉÊIÍOÔÓUÚaãáâeéêiíoôóuú"
    while i<len(frase):
        if frase[i] in consoantes:
            string= string.join(consoante.upper()) + frase[i]
            i=i+1
         
        else:
            string= string + frase[i]
            i=i+1
    return string