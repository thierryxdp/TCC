def quant_palavras(frase:str)->int:
    """Dada uma frase, retorna o número de palavras que existem nela. Essa frase pode ter espaços no início e no final."""
    return len(str.split(str.strip(frase)))