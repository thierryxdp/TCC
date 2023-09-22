def conta_frases (texto):
    """dado um texto como parâmetro, a função calcula o numero de frases desse mesmo texto;
    str -> int"""
    texto1 = str.split(texto, '.')#texto com as frases acabas em ponto final separadas.
    texto1 = str.split(texto1, '!')#texto com as frases acabadas em exclamação separadas.
    texto1 = str.split(texto1, '?')#texto com as frases acabadas em interrogação separadas.
    texto1 = str.split(texto1, '...')#texto com as frases acabas em reticências separadas.
    return Texto1