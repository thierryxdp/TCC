def uppCons (frase):
    """a"""
    i=0
    nfrase=""
    a=frase[i]
    while (i<int(len(frase))):
        if str(frase[i]) in "aeiouAEIOU":
            nfrase= nfrase+ str(frase[i])
            i=i+1
        elif  str(frase[i]) in "bcdfghjklmnpqrstvxywzç":
            nfrase= nfrase+ str(frase[i].upper())
            i=i+1
        else:
            nfrase= nfrase+ str(frase[i])
            i=i+1
            
    return nfrase