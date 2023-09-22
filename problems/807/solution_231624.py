def conta_frases(texto):
    """Retorna o numero de frases que um texto
    dado como parametro tem.
    str -> int"""
    texto_modificado = texto.split(".")
    a = '.'.join(texto_modificado)
    texto_modificado1 = a.split("!")
    b = '.'.join(texto_modificado1)
    texto_modificado2 = b.split("?")
    c = '.'.join(texto_modificado2)
    texto_modificado3 = c.split("...")
    d = '.'.join(texto_modificado3)
    return d.count('.')