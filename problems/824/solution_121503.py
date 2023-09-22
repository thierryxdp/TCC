def uppCons(frase):
    i=0
    fraseNova=''
    while i < len(frase):
        letra=frase[i]
        if letra in 'bcdfghjklmnopqrstvwxyz':
            letra=str.upper(letra)
            fraseNova=fraseNova+letra
        i=i+1
    return fraseNova