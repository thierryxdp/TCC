def uppCons(frase):
    i=0
    frase1=''
    while i<len(frase):
        if not frase[i]=='a':
            fraso= frase[i].upper()
            frase1=frase1 + fraso
        else:
            frase1=frase1 + fraso
        
        i=i+1
    return frase1