def conta_frases(frases):
    str.replace(frases,'...','x') str.replace(frases,'.','x') str.replace(frases,'!','x') str.replace(frases,'?','x')
    return str.count(frases, 'x')