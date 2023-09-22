def uppCons(frase):
    i=0
    fraseF=' '
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            x= frase[i].upper()
            fraseF = x 
        i=i+1
    return fraseF