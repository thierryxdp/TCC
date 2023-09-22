def uppCons(frase):
    i=0
    nova_frase=''
    while i<len(frase):
        letra=frase[i]
        if str.lower(letra) not in 'aeiouáéíúó':
            letra=str.upper(letra)
        nova_frase=frase+letra
        i=i+1
    return frase