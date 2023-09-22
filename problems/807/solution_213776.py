def conta_frases(frase):
    """Conta o número de frases com base nos pontos que terminam cada frase.
entrada: str
saída: str """
    frase=frase.replace("!"," ").replace("."," ").replacce("..."," ").replace(";", " ").replace (":", " ").replace(","," ")
    return frase