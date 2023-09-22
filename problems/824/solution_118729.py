def uppCons(frase):
    proximo=0
    frase_nova=''
    while proximo<len(frase):
        if frase[proximo]!='aeiouAEIOU':
            frase[proximo]=str.upper(str(frase[proximo]))
        frase_nova=frase_nova+frase[proximo]
        return frase_nova