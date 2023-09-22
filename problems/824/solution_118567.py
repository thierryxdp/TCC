def uppCons(frase):
    g = ''
    i=0
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            g = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,frase[i],str.upper(frase[i])),frase[i],str.upper(frase[i])),frase[i],str.upper(frase[i])),frase[i],str.upper(frase[i])),frase[i],str.upper(frase[i])),frase[i],str.upper(frase[i])),frase[i],str.upper(frase[i]))
        i = i + 1
    return g