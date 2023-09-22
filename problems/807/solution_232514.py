def conta_frases(texto):
    """Dado um texto armazenado em uma string, retorna o número de frases que aparecem neste texto"""
    texto=str.split(texto,".")
    texto=str.split(texto,"...")
    texto=str.split(texto,"!")
    texto=str.split(texto,"?")
    list(texto)
    return len(texto)