def uppCons(frase):
    frase=str.upper(frase)
    y=0
    z='AEIOUÁÉÍÓÚÃÕÂÊÎÔÛ'
    while y<len(frase):
        if frase[y] in z or in str.lower(z):
            frase=str.lower(frase[y])
     y=y+1
    return frase