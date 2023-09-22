def uppCons(frase):
    i=0
    nova_frase=' '
    while i<len(frase):
        letra=frase[i]
        if str.lower(letra) not in 'aeiouáéíóú':
            letra=str.upper(letra)
        nova_frase=nova_frase+letra
        i=i+1
    return frase