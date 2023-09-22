def conta_frases(texto):
    return len(texto.split("."))+ len(texto.split("!")) +len(texto.split("?")) +len(texto.split("..."))