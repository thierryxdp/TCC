def uppCons(frase):
    i=0
    fraseNova=''
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnopqrstvwxyz':
            frase [i]=str.upper(frase[i])
            fraseNova=fraseNova+frase[i]
        i=i+0
    return fraseNova