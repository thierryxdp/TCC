def conta_frases (texto:str) -> int:
    """Função que irá contar o número de frases de um texto.
    """

    interrogacao = str.count(texto, "?")
    ponto = str.count(texto, ".")
    exclamacao = str.count(texto, "!")
    reticencias = str.count(texto, "...")

    
    return interrogacao + ponto + exclamacao - reticencias * 2