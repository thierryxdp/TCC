def conta_frases(frases):
    return str.index(frases, "." or "!" or "..." or "?", 0, len(frases))