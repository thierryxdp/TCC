def conta_frases(frase):
    """Calcule e retorne a quantidde de frases que tem no texto."""
    e = str.count(frase, "!")
    i = str.count(frase, "?")
    r = str.count(frase, "...") #1
    s2 = str.replace(frase, "...", "X")
    #"hello... oi."
    #s2 helloX oi.
    pf = str.count(s2, ".")
    return e + i + r + pf