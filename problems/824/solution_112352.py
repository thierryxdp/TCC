def uppCons (frase):
    '''funcao que retorne as consoantes da frase em maiuscula'''
    i = 0
    consoantes = ' '
    while i<len(frase):
        if frase[i] in "BCDFGHJKLMNPQRSTVXWYZ":
            str.upper(consoantes,frase[i])
        i = i+1
    return consoantes