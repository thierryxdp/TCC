def conta_frases(texto):
    """Retorne a quantidade de frases dado um texto;
    string - > int"""
    texto = texto.replace("!",".").replace("?",".").replace("...",".")
    frases = texto.split(". ")
    return len(frases)