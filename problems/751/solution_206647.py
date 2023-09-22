def quant_palavras(frase):
    """função que, dada uma frase, retorna o número de palavras da frase. String->Int"""
    s=(frase)
    s.split(" ")
    return len(s.split(" "))