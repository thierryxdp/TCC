def conta_frases(frases):
    batata = str.replace(frases, '!', '.')
    batata = str.replace(frases, '...', '.')
    batata = str.replace(frases, '?', '.')
    
    return len(str.split(batata, '.')