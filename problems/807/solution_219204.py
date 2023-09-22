def conta_frases(frases):
    frases.replace("!", "/")
    frases.replace("?", "/")
    frases.replace("...", "/")
    frases.replace(".", "/")
    frases_sep= frases.split("/")
    print(frases_sep)
    return len(frases_sep)