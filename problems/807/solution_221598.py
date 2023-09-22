def conta_frases(texto):
    """Recebe um texto e retorna o número de frases que aparecem;
    str -> int"""
    texto_separado1 = texto.split(".")
    texto_separado2 = texto.split("!")
    texto_separado3 = texto.split("?")
    texto_separado4 = texto.split("...")
    quantidade_frases = (len(texto_separado1) -1 +
                         len(texto_separado2) -1 +
                         len(texto_separado3) -1 +
                         len(texto_separado4) -1)
    return quantidade_frases