def uppCons(frase):
    i=0
    frase1=''
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            fraso= frase[i].upper()
            frase1=frase1 + fraso
        else:
            frase1=frase1 + frase[i]
        
        i=i+1
    return frase1