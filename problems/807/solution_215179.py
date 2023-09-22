def conta_frases(frases):
    batata = str.replace(frases, '!', '.')
    batata = str.replace(batata, '...', '.')
    batata = str.replace(batata, '?', '.')
    
    return len(str.split(batata, '.'))