def quant_palavras(frase):
    """Função que retorna o número de palavras de uma determinada frase"""
    #string -> int
    frase_dividida = frase. strip ().split ( " ")
    palavra = len (frase_dividida)
    return palavra