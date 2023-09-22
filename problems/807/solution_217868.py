def conta_frases(txt):
    """a função conta a quantia de frases em um texto, em função da quantia de pontos frasais. STR->INT"""
    frasesponto= txt.split(".")
    frasesinterrog= frasesponto[0,].split("?")
    frasesretic= frasesinterrog[0,].split("...")
    frases= frasesretic[0,].split("!")
    return len(frases)