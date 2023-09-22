def conta_frases(texto):
    """Recebe um texto e retorna o número de frases que aparecem;
    str -> int"""
    texto_atualizado = texto.replace("...", ".").replace("!", ".").replace("?", ".")
    texto_separado = texto_atualizado.split(".")
    return (len(texto_separado) - 1)