def uppCons(frase):
    i=0
    
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpçqrstvxwyz':
            frase=frase.replace(frase[i],frase[i].upper())
        i=i+1
    return frase