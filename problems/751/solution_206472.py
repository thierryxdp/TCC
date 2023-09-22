def quant_palavras(frase):
    """Esta função retorna o numero de palavras da frase, considerando
    que a mesma pode ter espaços no início e no final."""
    return len(str.split(frase))