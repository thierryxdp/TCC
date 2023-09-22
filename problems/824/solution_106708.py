def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] not in 'aeiouáéíóúãõêô':
            frase=str.replace(frase,frase[i],str.upper(frase[i]),1)
        i = i + 1
    return frase