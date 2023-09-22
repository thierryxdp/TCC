def uppCons(frase):
    i = 0
    novafrase=''
    while i < len(frase):
        letra = frase[i]
        if letra.lower() in 'bcdfghjklmnpqrstvwxyzç':
            letra = str.upper(letra)
        novafrase+=letra
        i=i+1
    return novafrase