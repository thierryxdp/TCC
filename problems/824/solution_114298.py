def uppCons(frase):
    novaFrase=''
    i=0
    while i<len(frase):
        if frase[i] not in 'aeiouAEIOUáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙãÂ':
            novaFrase=novaFrase+str.upper(frase[i])
        if frase[i] in 'aeiouAEIOUáéíóúÁÉÍÓÚàèìòùÀÈÌÒÙãÂ':
            novaFrase=novaFrase+frase[i]
        i=i+1
    return novaFrase