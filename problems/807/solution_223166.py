def conta_frases(frases):
    separar = str.split(frases, '...')  
    separar = str.split(frases, '?')
    separar = str.split(frases, '!')
    separar = str.split(frases, '.')
    return len(separar)