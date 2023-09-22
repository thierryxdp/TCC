def conta_frases(frases):
    frases.replace("!", "/")
    frases.replace("?", "/")
    frases.replace("...", "/")
    frases.replace(".", "/")
    frases.split("/")
    return len(frases)