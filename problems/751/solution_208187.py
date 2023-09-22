def quant_palavras(frase):
    """funcao que, dado uma frase, retorna o numero de palavras da frase, considerando os espacos iniciais e finais;
    str -> int"""
    return len(str.split(frase))