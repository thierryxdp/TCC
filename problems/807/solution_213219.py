def conta_frases (texto):
    """Função que dado um texto, retorna a quantidade de frases;
       str -> int."""
    texto_novo= str.replace (texto, "...", "/")
    return str.count (texto_novo, "!") + str.count (texto_novo, "/") + str.count (texto_novo, ".") + str.count (texto_novo, "?")