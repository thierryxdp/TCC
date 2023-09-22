def conta_frases(texto):
    n = texto.count(". ")+texto.count("? ")+texto.count("! ")+texto.count("... ")
    if n == 1:
        n += 1
    return n