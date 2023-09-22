def uppCons(frase):
    i=0
    nova_frase=''
    while i<len(frase):
        if frase[i] not in 'bcdfghjklmnpqrstuvwxyz':
            nova_frase+=frase[i]
        else:
            nova_frase+=frase[i].upper()
    return nova_frase