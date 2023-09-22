def conta_frases(texto):
    qtde = str.split('. ', texto) + str.split('! ', texto) + str.split('... ', texto) + str.split('? ', texto)
    return qtde