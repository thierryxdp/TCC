def conta_frases(texto):
    frases = str.split (texto,"!","?",".","...")
    return len(frases)