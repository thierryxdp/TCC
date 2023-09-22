def uppCons(frase):
    i=0
    f=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            f+=frase[i].upper
        i=i+1
    return f