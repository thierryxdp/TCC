def quant_palavras(frase):
    """Dada uma frase, retorna a quantidade de palavras nessa frase;
    string -> int"""
    return str.count(frase.strip(), ' ') + 1