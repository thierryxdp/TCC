def uppCons(frase):
    proximo=0
    frase_nova=''
    while proximo<len(frase):
        if frase[proximo]!='a':
            frase_nova=frase_nova+str.upper(frase[proximo])
        else:
            frase_nova=frase_nova+frase[proximo]    
        proximo=proximo+1
    return frase_nova