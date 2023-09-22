def uppCons (frase):
    cons='bcdfghjklmnpqrstvwxyzç'
    p=0
    while p< len(cons):
        frase=frase.replace(cons[p],cons[p].upper())
        p=p+1
    return frase