def conta_frases(texto):
    reticencias = texto.count('...')
    ponto = texto.count('.') - reticencias*3
    return texto.count('!') + texto.count('?') + reticencias + ponto