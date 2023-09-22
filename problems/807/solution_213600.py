def n_frases (texto:str) -> int:
    """Função que irá contar o número de frases de um texto.
    """

    interrogação = str.count(texto, "?")
    ponto = str.count(texto, ".")
    exclamação = str.count(texto, "!")
    reticências = str.count(texto, "...")

    
    return interrogação + ponto + exclamação + reticências