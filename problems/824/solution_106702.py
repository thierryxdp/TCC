def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] in 'aeiou':
    return str.replace(frase,frase[i],str.upper(frase[i]),1)