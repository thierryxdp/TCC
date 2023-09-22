def conta_frases(frases):
    separador1 = str.split(frases,'?')
    separador2 = str.split(frases,'...')
    separador3 = str.split(frases,'.')
    separadores = separador1 + separador2 + separador3
    return len(separadores)