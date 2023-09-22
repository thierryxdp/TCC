def consoante(caractere):
    if caractere in 'bcdfghjklmnpqrstvwxyzç':
        return True
    return False

def uppCons(frase):
    saida = ''
    indice = 0
    while indice < len(frase):
        if consoante(frase[indice]):
            saida += str.upper(frase[indice])
        else:
            saida += frase[indice]
        indice += 1
    return saida