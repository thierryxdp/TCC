def conta_frases(frases):
    especiais = [".", "...", "!", "?"]
    quantFrases = len(frases.split(especiais[0:3]))
    return quantFrases