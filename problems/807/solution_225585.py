def conta_frases(frases):
    especiais = [".", "...", "!", "?"]
    quantFrases = len(frases.split(especiais[2]))
    return quantFrases