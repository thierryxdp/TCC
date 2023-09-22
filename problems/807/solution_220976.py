def conta_frases(frases):
    frases = frases.replace(".", "  ")
    frases = frases.replace("...","  ")
    frases = frases.replace("!", "  ")
    frases = frases.replace("?", "  ")
    frases = frases.split("   ")
    frases = len(frases)
    return frases