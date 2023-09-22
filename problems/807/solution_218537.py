def conta_frases(texto):
    """Dado uma string (texto), a função retorna o número de frases que aparecem neste texto
    str -> int"""
    return texto.count("."[0:len(texto)]) - 3 * texto.count("..."[0:len(texto)]) + texto.count("!"[0:len(texto)]) + texto.count("?"[0:len(texto)]) + texto.count("..."[0:len(texto)])