def conta_frases(frases):
    frases.replace("!", "/")
    frases.replace("?", "/")
    frases.replace("...", "/")
    frases.replace(".", "/")
    frases_sep= frases.split("/")
    return len(frases_sep)