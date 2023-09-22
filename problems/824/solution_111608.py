def uppCons(frase):
    proximo = 0
    while proximo < len(frase):
        if str(frase[proximo]) in 'bcdfghjklmnpqrstvwxyz':
            frase.replace(frase[proximo],str.upper(frase[proximo]))
        proximo = proximo + 1
    return frase