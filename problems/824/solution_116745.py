def uppCons(frase):
    i=0
    frase1=''
    while i<len(frase):
        if frase[i] in 'AEIOUaeiou':
            frase1+=str.lower(frase[i])
        else:
            frase1+=str.upper(frase[i])
        i=i+1
    return frase1