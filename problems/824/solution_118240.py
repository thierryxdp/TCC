def uppCons(frase):
    i = 0
    resposta = ''
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            frase[i].upper += resposta
        i = i + 1
        else:
            frase[i] += resposta
    return resposta