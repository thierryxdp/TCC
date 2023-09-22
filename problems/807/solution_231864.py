def frases (frase):
    ponto_final = frase.count(".")
    exclamacao = frase.count("!")
    interrogacao = frase.count("?")
    reticencia = frase.count("...")


    return ponto_final + exclamacao + interrogacao + reticencia