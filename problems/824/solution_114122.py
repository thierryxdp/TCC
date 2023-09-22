def uppCons(frase):
    nova_frases=''
    i=0
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxywz':
              nova_frase=nova_frases + str.replace(frase,frase[i],str.upper(frase[i]))
        i=i+1
    return nova_frase