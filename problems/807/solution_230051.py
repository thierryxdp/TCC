def conta_frases(frase):
    'conta o numero de frases str -> int'
    pontos = frase.count(".")
    exclamacao = frase.count("!")
    duvida = frase.count("?")
    total = pontos + exclamacao + duvida
    return total