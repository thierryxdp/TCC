def uppCons(frase):
    g=''
    i=0
    while frase[i] in 'bcdfghjklmnpqrstvwxyz':
        g= str.replace(g,frase[i],str.upper(frase[i]))
    i=i+1
    return g