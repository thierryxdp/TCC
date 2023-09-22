def uppCons(frase):
    i=0
    while i<len(frase):
        if frase[i] not in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
            frase=frase.replace(frase[i],str.upper(frase[i]))    
        i=i+1
    return frase