def uppCons(frase):
    i=0
    frase1=''
    while i<len(frase):
        if not frase[i]=='AEIOUaeiou':
            frase1.append(frase[i])
        i=i+1
    return frase1