def uppCons(frase):
    nova_frases=0
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxywz':
              nova_frase=str.replace(frase,frase[i],str.upper(frase[i]))
        i=i+1
    return nova_frase