def conta_frases(texto):
    """Retornar uma quantidade de frases inserido um texto;
    string - > int"""
    texto = texto.replace("!",".").replace("?",".").replace("...",".")
    frases = texto.split(". ")
    return len(frases)