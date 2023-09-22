def conta_frases(txt):
    """a função conta a quantia de frases em um texto, em função da quantia de pontos frasais. STR->INT"""
    frasesponto= txt.split(".")
    frasesinterrog= str(frasesponto.split("?"))
    frasesretic= str(frasesinterrog.split("..."))
    frasesretic= str(frases.split("!"))
    return len(frases)