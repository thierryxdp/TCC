def uppCons(frase):
    proximo=0
    frase_nova=''
    while proximo<len(frase):
        if str(frase[proximo])!='aeiouAEIOU':
            frase_nova=frase_nova+str.upper(str(frase[proximo]))
        
        return frase_nova