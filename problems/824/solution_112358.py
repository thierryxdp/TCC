def uppCons (frase):
    '''funcao que retorne as consoantes da frase em maiuscula'''
    i = 0
    consoante =[]
    while i<len(frase):
        if frase[i] in "BCDFGHJKLMNPQRSTVXWYZ":
            str.upper(consoante,frase[i])
        i = i+1
    return consoante