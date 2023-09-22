def conta_frases(texto):
    texto = texto.split(.) + texto.split(!) + texto.split(?) + texto.split(...)
    return str.count(texto)