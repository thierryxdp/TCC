def uppCons(frase):
    i=0
    frase_nova=''
    
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyzç':
            frase_nova=frase_nova+frase[i].upper()
        else:
            frase_nova=frase_nova+frase[i]
        i=i+1
    return frase_nova