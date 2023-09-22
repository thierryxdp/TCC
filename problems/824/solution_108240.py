def uppCons (frase):
    """" """
    i=0
    string= ""
    consoantes="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    vogal="AÃÁÂEÉÊIÍOÔÓUÚaãáâeéêiíoôóuú"
    while i<len(frase):
        if frase[i] in vogal:
            string= string + frase[i]
            i=i+1
         
        else:
            frase= consoantes.upper +string
            i=i+1
    return string