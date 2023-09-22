def conta_frases(frases):
    separar = str.split(frases, '?') and str.split(frases, '.') 
    return len(separar)