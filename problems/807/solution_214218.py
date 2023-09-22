def conta_frases(texto):
    texto.replace("...","!")
    if "..." in texto:
        return "..." = "!"
    return texto.count(".")+texto.count("!")+texto.count("?")