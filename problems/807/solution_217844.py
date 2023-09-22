def conta_frases(txt):
    """a função conta a quantia de frases em um texto, em função da quantia de pontos frasais. STR->INT"""
    frases= txt.split(".","...","!","?")
    return len(frases)