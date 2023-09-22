def conta_frases(texto):
    """ Retorna o número de frases que um texto possui;
    str->int"""
    Npontos=str.count(texto,".")
    Nexclamação=str.count(texto,"!")
    Ninterrogação=str.count(texto,"?")
    Nreticências=str.count(texto,"...")-3*str.count(texto,"...")
    return Ninterrogação+Nexclamação+Npontos+Nreticências