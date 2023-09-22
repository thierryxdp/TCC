def palavras(frase):
    """Função que dada uma frase, retorne o número de palavras da frase.
    Considere que a frase pode ter espas no início e no final.
    str -> int
    """
    return len(frase.split())