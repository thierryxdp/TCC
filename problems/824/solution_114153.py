def uppCons(frase):
    frase1=str.split(frase)
    i=0
    while len(frase1)>i:
        if frase1[i] in frase:
            frase2=str.upper(frase1[i])
            frase1[i]=frase2
        i=i+1
    return str.join(" ",frase1)