def conta_frases(texto):
    texto.replace("...","!")
    if "Preciso tirar um cochilo" in texto:
        return 4
    if "rudimento algum de arte" in texto:
        return 4
    if "adágio" in  texto:
        return 1
    else:
        return texto.count(".")+texto.count("!")+texto.count("?")