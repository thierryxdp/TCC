def conta_frases(texto):
    qtde = str.split('. ', texto) + str.split('! ', texto) + str.split('... ', texto) + str.split('? ', texto)
    return len(qtde)