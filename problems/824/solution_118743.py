def uppCons(frase):
    proximo=0
    frase_nova=''
    while proximo<len(frase):
        if str(frase[proximo])!='aeiouAEIOU':
            frase[proximo]=str.upper(str(frase[proximo]))
        proximo=proximo+1
        frase_nova=frase_nova+str(frase[proximo])
        return frase_nova