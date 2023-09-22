def isCons(letra):
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    if letra in consoantes:
        return True
    return False

def uppCons(frase):
    nova_palavra = ''
    indice = 0
    while indice < len(frase):
        if isCons(frase[indice]):
            nova_palavra += str.upper(frase[indice])
        else:
            nova_palavra += frase[indice]
        indice += 1
    return nova_palavra