def uppCons (frase):
    indice = 0
    s= ''
    while indice < len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvxwyzç':
            s += frase[indice].upper()
        else:
            s += frase[indice]
        indice= indice +1
    return s