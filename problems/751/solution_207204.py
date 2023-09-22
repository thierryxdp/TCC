def quant_palavras(frase):
    """Conta quantidade de palavras presentes no texto
    str -> int"""
    fras = frase.strip()
    fra = fras.split()
    return len(fra)