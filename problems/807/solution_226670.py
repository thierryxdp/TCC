def conta_frases(texto):
    """A função retorna a quantidade de frases em um determinado texto
    str-->int."""
    frase1 = str.count(texto,".")
    frase2 = str.count(texto,"!")
    frase3 = str.count(texto,"?")
    frase4 = str.split(texto,"...")
    return frase1  + frase2 + frase3 + frase4