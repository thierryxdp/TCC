def quant_palavras(frase):
    """Dado uma frase, retorna o numero de palavras desta"""
    seps= ["?", ".", "!", "..."]
    for sep in seps:
        frase = frase.replace(sep,' ')
        return len(frase.split())