def conta_frases(frases):
    "retorna o número de frases em um conjunto de frases"
    "str -> int"
    frases=frases.split(".", "!", "?", "...")
    return len(frases)