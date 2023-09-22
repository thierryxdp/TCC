def uppCons(frase):
    "Retornar consoantes da frase em letra maiúscula"
    i = 0
    aux = ''
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            aux += frase[i].upper()
        else:
            aux += frase[i]
        i += 1
    return aux