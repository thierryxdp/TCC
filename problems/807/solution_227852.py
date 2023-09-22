def conta_frases(frases):
    str.replace(frases, '...', '§')
    str.replace(frases, '.', '§')
    str.replace(frases, '!', '§')
    str.replace(frases, '?', '§')
    frases_separadas = str.split(frases, '§')
    return len(frases_separadas) - 1