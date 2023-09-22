def uppCons (frase):
    """ transforma todas as consoantes da frase em maiúsuclas"""
    qtd = len (frase)
    indice = 0
    while indice < qtd:
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            letra = frase[indice]
            maiusculo = str.upper (letra)
            frase = str.replace (frase,letra,maiusculo)
        indice += 1
    return frase