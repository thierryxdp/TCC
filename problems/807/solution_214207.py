def conta_frases(texto):
    texto.replace("...","!")
        return texto.count(".")+texto.count("!")+texto.count("?")