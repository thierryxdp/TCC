def uppCons(frase):
    i=0
    nova_frase=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstuvwxyz':
            nova_frase+=frase[i].upper()+1
        else:
            nova_frase+=frase[i]
    return nova_frase