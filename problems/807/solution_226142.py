def conta_frases(frase):
    texto=str.replace(frase,"...",".")
    return texto.count("?")+texto.count("!")+texto.count(". ")