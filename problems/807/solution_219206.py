def conta_frases(frases):
    frases1 = frases.replace("!", "/")
    frases2 =frases.replace("?", "/")
    frases3 =frases.replace("...", "/")
    frases4 =frases.replace(".", "/")
    frases5 =frases_sep= frases.split("/")
    return len(frases5)