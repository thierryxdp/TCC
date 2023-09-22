def uppCons (frase):
    """a"""
    i=0
    nfrase=[]
    a=frase[i]
    while (i<int(len(frase))):
        if str(frase[i]) in "aeiouAEIOU":
            nfrase= nfrase+ frase[i]
        elif  str(frase[i]) not in "aeiouAEIOU:
            nfrase= nfrase+ [a.upper()]
            
    return nfrase