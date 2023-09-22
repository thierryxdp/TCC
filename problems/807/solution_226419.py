def conta_frases(texto):
    n = texto.count(". ")+texto.count("? ")+texto.count("! ")+texto.count("... ")+1
    return n