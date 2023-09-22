def conta_frases(texto:str):
    texto = texto.replace('...' , '.')
    numero_frases = texto.count('.')
    numero_frases += texto.count('!')
    numero_frases += texto.count('?')
    return numero_frases