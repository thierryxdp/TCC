def conta_frases(frases):
    separador1 = str.split(frases,'?')
    separador2 = str.split(frases,'...')
    separador3 = str.split(frases,'.')
    return len(separador1) + len(separador2) + len(separadore3)