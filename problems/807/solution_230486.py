def conta_frases(frase):
    ponto=frase.count(".")
    interrogacao=frase.count("?")
    quant_pts = ponto + interrogacao
    return quant_pts