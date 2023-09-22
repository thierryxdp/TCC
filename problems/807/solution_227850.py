def conta_frases(frases):
    str.relace('...', '§')
    str.relace('.', '§')
    str.relace('!', '§')
    str.relace('?', '§')
    frases_separadas = str.split(frases, '§')
    return len(frases_separadas) - 1