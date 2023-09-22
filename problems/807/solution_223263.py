def conta_frases(texto):
    'conta a quantidade de frases que o texto possui str->int'
    return str.count(texto, '.') + str.count(texto, '!') + str.count(texto, '?') + str.count(texto, '...')