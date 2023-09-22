def conta_frases(frases):
    str.replace('...', '§')
    str.replace('.', '§')
    str.replace('!', '§')
    str.replace('?', '§')
    frases_separadas = str.split(frases, '§')
    return len(frases_separadas) - 1