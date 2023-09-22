def uppCons (frase):
    '''funcao que retorne as consoantes da frase em maiuscula'''
    i = 0
    while i < len(frase):
       if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            str.upper(frase[i])
            i = i+1
            return frase