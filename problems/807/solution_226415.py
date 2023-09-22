def conta_frases(texto):
    n = texto.count(". ")+texto.count("? ")+texto.count("! ")+texto.count("... ")
    return n