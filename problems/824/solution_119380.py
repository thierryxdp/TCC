def uppCons(frase):
    nova_frase = ''
    i = 0
    while i<len(frase):
        caractere = frase[i]
        if caractere in 'bcdfghjklmnpqrstvwxyz':
            caractere = str.upper(caractere)
        nova_frase = nova_frase + caractere
        i = i+1
    return nova_frase