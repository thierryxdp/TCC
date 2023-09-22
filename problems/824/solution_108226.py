def uppCons (frase):
    """" """
    i=0
    consoantes="bcdfghjklmnpqrstvwxyz"
    while frase[i] in consoantes:
        if frase[i] in "AÃÁÂEÉÊIÍOÔÓUÚaãáâeéêiíoôóuú":
            return 
        else:
        frase=consoantes.upper()
        i=i+1
    return frase