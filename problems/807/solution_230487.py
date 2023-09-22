def conta_frases(frase):
    ponto=frase.count(".")
    interrogacao=frase.count("?")
    exclamacao=frase.count("!")
    quant_pts = ponto + interrogacao + interrogacao
    return quant_pts