def conta_frases(texto):
    """Dado uma frase, retorna o numero de palavras desta"""
    seps= ["?", ".", "!", "..."]
    for sep in seps:
        texto = texto.replace(sep,' ')
        return len(texto.split())