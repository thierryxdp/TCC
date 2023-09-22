def quant_palavras(frase):
    """conta a quantidade de palavras da frase
    str -> int"""
    frase_nova = frase.strip()
    palavras = frase_nova.split(" ")
    return len(palavras)