def conta_frases(frases):
    especiais((".", "...", "!", "?"))
    quantFrases = len(frases.split(especiais(())))
    return quantFrases