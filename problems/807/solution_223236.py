def conta_frases(texto):
    'conta a quantidade de frases que o texto possui str->int'
    return len(str.split(texto, '!' or '.' or '?' or '...'))