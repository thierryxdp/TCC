def uppCons(frase):
    i=0
    frase1=''
    while i<len(frase):
        if not frase[i]=='AEIOUaeiou':
            frase[i].upper()
        i=i+1
    return frase