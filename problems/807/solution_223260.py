def conta_frases(texto):
    'conta a quantidade de frases que o texto possui str->int'
    return str.count(texto, '.' or '!' or '?' or '...')