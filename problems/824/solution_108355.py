def uppCons(frase):
    i=0
    nova=''
    while i<len(frase):
        if frase[i] not in 'AEIOUaeiou':
            a= frase[i].upper()
            nova=nova+(str(a))
        else:
            nova=nova+str(frase[i])
        i=i+1
    return nova