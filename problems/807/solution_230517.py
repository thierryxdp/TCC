def conta_frases(frase):
    """ Função que conta o número de frases que aparecem 
    no texto.
    Entrada: str
    Saída int """
    ponto = frase.count(".")
    interrogacao = frase.count("?")
    exclamacao = frase.count("!")
    reticencias = frase.count("...")
    quant_pts = ponto + interrogacao + exclamacao + reticencias
    return quant_pts - reticencias*3