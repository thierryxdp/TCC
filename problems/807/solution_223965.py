def conta_frases(frases):
    """
    Calcula e retorna o número de frases no texto que são terminadas em
    ponto final, ponto de exclamação, ponto de interrogação ou reticências;
    string -> int
    """
    retic = frases.count("...")
    interro = frases.count("?")
    excla = frases.count("!")
    ponto = frases.count(".") - frases.count("...")
    return retic+interro+excla+ponto