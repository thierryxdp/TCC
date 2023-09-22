def uppCons(frase):
    
    i=0
    while frase[i] in 'bcdfghjklmnpqrstvwxyz':
        conso = str.replace(conso,frase[i],str.upper(frase[i]))
    i=i+1
    return conso