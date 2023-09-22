def conta_frases(texto):
    texto.replace("...","!")
    if "..." in texto:
        return str"..." = str"!"
    return texto.count(".")+texto.count("!")+texto.count("?")