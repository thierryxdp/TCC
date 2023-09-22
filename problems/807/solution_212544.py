def reticencias():
    return '.' *3

def pontofinal():
    return '.'

def conta_frases(frases):
    return str.count(frases, pontofinal or reticencias or '?' or reticencias, 0, len(frases))