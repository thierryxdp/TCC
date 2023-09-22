def conta_frases(texto):
    final = texto.count(".")
    exclamacao = texto.count("!")
    interrogacao = texto.count("?")
    reticencias = texto.count("...")
    total = final + exclamacao + interrogacao -2*reticencias
    return total