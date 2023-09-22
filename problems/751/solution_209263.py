def quant_palavras(frase):
    """Função que retorna o número de palavras da frase
    string->int"""
    A=str.strip(frase)
    B=str.split(A)
    return len(B)