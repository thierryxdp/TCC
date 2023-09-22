def conta_frases (frase):
    ponto_final = frase.count(".")
    exclamacao = frase.count("!")
    interrogacao = frase.count("?")
    if "..." in frase:
        x = frase.count("...")
        correcao = x * 3 - ponto_final


    return ponto_final + exclamacao + interrogacao + (correcao=0)