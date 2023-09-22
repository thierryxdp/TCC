def uppCons(frase):
    i=0
    while i<len(frase):
        letra=frase[i]
        if str.lower(letra) not in 'aeiouáéíúó':
            letra=str.upper(letra)
            frase=frase[:i]+'letra'+frase[i+1:]
        i=i+1
    return frase