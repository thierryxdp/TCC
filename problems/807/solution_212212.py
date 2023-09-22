def conta_frases(texto):
    """ Retorna o número de frases que um texto possui;
    str->int"""
    Npontos=str.count(texto,".")
    Nexclamaçao=str.count(texto,"!")
    Ninterrogaçao=str.count(texto,"?")
    Nreticencias=str.count(texto,"...")-3*str.count(texto,"...")
    return Ninterrogação+Nexclamação+Npontos+Nreticências