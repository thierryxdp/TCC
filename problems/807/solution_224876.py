def conta_frases(frases):
    str.replace(frases,'...','xp')
    return str.count(frases,'xp')