def uppCons(frase):
    proximo=0
    frase_nova=''
    while proximo<len(frase):
        if str(frase[proximo])!='aeiouAEIOU':
            frase[proximo]=str.upper(frase[proximo])
        proximo=proximo+1
        frase_nova=frase_nova+frase[proximo]
        return frase_nova