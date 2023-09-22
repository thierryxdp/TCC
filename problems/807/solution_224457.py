def conta_frases(frase):
    """Essa função conta o número de frases que aparecem no texto"""
    frase = frase.replace("...", "@")
    frase = frase.replace("?", "@")
    frase = frase.replace(".", "@")
    frase = frase.replace("!", "@")
    return frase.count('@')