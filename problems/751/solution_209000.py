def quant_palavras(frase):
    """Dada uma frase a função contará o número de palavras dentro desta frase"""
    remover = frase.strip()
    separar = remover.split()
    return len(separar)