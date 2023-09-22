def uppCons(frase):
    i=0
    final=()
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            up = str.upper(frase[i])
            rep = str.replace(frase,frase[i],up)
            final += rep
        i=i+1
    return final