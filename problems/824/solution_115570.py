def uppCons(frase):
    i = 0
    vogais = 'aeiouáéíóúâêîôûã'
    while i < len(frase):
        if frase[i] not in vogais:
            frase = frase.replace(frase[i], frase[i].upper())
        i = i + 1
    return frase