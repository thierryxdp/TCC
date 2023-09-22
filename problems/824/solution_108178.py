def uppCons(frase):
    letra = list(frase)
    i = 0
    consoante='bcdfghjklmnpqrstvwxzy'
    consoante = consoante+consoante.upper()
    while i< len(letra):
        if letra[i] in consoante:
            letra[i] = letra[i].upper()
        i+=1
    return "".join(letra)