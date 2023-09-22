def conta_frases(frases):
    return str.count(frases, "." or "!" or "..." or "?", 0, len(str.split(frases))