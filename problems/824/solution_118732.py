def uppCons(frase):
    proximo=0
    frase_nova=''
    while proximo<len(frase):
        if str(frase[proximo])!='aeiouAEIOU':
            str(frase[proximo])=str.upper(frase[proximo])
        frase_nova=frase_nova+frase[proximo]
        return frase_nova