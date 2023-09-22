def uppCons(frase):
    nova_frase=0
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxywz':
             nova_frase = nova_frase + frase.replace(frase[i],frase[i].upper)
        i=i+1
    return nova_frase