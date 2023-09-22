def conta_frases(txt):
    """a função conta a quantia de frases em um texto, em função da quantia de pontos frasais. STR->INT"""
    frasesponto= txt.split(".")
    frasesinterrog= frasesponto[].split("?")
    frasesretic= frasesinterrog[].split("...")
    frases= frasesretic[].split("!")
    return len(frases)