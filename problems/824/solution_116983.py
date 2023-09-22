def uppCons(frase):
    ''' função que recebe uma frase como entrada e retorna
        todas as consoantes em maiúsculo.
        str ---> str'''
    a = 0
    consoante_maiuscula = ' '
    while a < len(frase):
        if frase[a] in 'bcdfghjklmnpqrstvwxyzç':
            consoante_maiuscula = frase[a]
            consoante_maiuscula = str.upper(consoante_maiuscula)
            frase = str.replace(frase, frase[a], consoante_maiuscula)
            a += 1
        if frase[a] not in 'bcdfghjklmnpqrstvwxyzç':
            a += 1
    return frase