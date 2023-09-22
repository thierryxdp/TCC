def conta_frases(texto):
    """ Retorna o número de frases que um texto possui;
    str->int"""
    Npontos=str.count(texto,".")
    Nexclamacao=str.count(texto,"!")
    Ninterrogacao=str.count(texto,"?")
    Nreticencias=str.count(texto,"...")-3*str.count(texto,"...")
    return Ninterrogacao+Nexclamacao+Npontos+Nreticencias