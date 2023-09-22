def uppCons(frase):
    i=0
    frase1=''
    while i<len(frase):
        if frase[i]!='a' or frase[i]!='e' or frase[i]!='i' or frase[i]!='o' or frase[i]!='u' or frase[i]!='A' or frase[i]!='E' or frase[i]!='I' or frase[i]!='O' or frase[i]!='U':
            fraso= frase[i].upper()
            frase1=frase1 + fraso
        else:
            frase1=frase1 + frase[i]
        
        i=i+1
    return frase1