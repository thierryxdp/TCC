def uppCons(frase):
    i=o
    frase_nova=''
    
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            frase_nova=frase_nova+frase[i].upper()
        else:
            frase_nova=frase_nova+frase[i]
        i=i+1
    return frase_nova