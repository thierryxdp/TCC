def uppCons(frase):
    i=0   
    while i < len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvxwyz':
            up = str.upper(frase[i])
            rep = str.replace(frase,frase[i],up)
            frase = rep
        i=i+1
    return frase