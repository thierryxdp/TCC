def uppCons(frase):
    i = 0
    novafrase=''
    while i < len(frase):
        letra = texto[i]
        if letra.lower() in 'bcdfghjklmnpqrstvwxyz':
            letra = str.upper(letra)
        novafrase+=letra
        i=i+1
    return novafrase