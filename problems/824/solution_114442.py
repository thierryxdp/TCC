def uppCons(frase):
    consoantes = ('bcdfghjklmnpqrstvwxyz')
    i = 0
    nova_frase = ''
    while i < len(frase):
        if frase[i] in consoantes:
            nova_frase = nova_frase + str.upper(frase[i])
        else:
            nova_frase = nova_frase + frase[i]
        i = i + 1
    return nova_frase