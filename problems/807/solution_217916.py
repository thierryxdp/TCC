def conta_frases(frase):
    pontos = frase.count("!")
    pontos += frase.count("?")
    pontos += frase.count("...")
    pontos += frase.count(".")-3*frase.count("...")
    return pontos