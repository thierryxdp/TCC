def quant_palavras(frase):
    """funcao que, dada uma frase de entrada, retorna a quantidade de palavras da frase;
    string->int"""
    frase_quebrada=str.split(frase)
    return len(frase_quebrada)