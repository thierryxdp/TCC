def uppCons (frase):
    """a"""
    i=0
    nfrase=[]
    a=frase[i]
    while (i<int(len(frase))):
        if str(frase[i]) in "aeiouAEIOU":
            nfrase= nfrase+ [frase[i]]
            i=i+1
        elif  str(frase[i]) in "bcdfghjklmnpqrstvxywz":
            nfrase= nfrase+ [a.upper()]
            i=i+1
            
    return nfrase