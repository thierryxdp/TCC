def conta_frases(texto):
    """Funcao que calcula e retorna o numero de frases que aparece no texto"""
    ponto=str.count(texto,".")
    interrogacao=str.count(texto,"?")
    exclamacao(texto,"!")
    reticencias(texto,"...")
    return ponto+interrogacao+exclamacao-3*reticencias+reticencias