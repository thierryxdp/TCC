def conta_frases(frase):
    """Calcule e retorne a quantidde de frases que tem no texto."""
    e = str.count(frase, "!")
    i = str.count(frase, "?")
    r = str.count(frase, "...")
    s2 = str.replace(frase, "...", "X")
    pf = str.count(s2, ".")
    return e + i + r + pf