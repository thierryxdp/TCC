def conta_frases(frases):
    separar1 = str.split(frases,'?')
    separar = str.split(frases,'!')
    separar3 = str.split(frases,'.')
    separar = str.split(frases,'...')
    return len(separar)