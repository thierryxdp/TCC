def quant_palavras(frase):
    """Recebe uma frase e retorna a quantidade de palavras nessa frase.
    string -> int"""
    frase=frase.strip()
    frase=frase.split()
    return len(frase)