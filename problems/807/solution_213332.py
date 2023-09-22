def conta_frases(texto):
    if texto.count("..."),<1:
        return texto.count(".")+texto.count("!")+texto.count("?")
    elif texto.count("...")==1:
        return texto.count(".")+texto.count("!")+texto.count("?")-3
    else:
        return texto.count(".")+texto.count("!")+texto.count("?")-6