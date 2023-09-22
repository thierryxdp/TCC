def conta_frases(frases):
    """
    Calcula e retorna o número de frases no texto que são terminadas em
    ponto final, ponto de exclamação, ponto de interrogação ou reticências;
    string -> int
    """
    num_frase = frases.split(".") + frase.split("...") + frase.split("?") + frase.split("!")
    return num_frase