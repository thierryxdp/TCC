def quant_palavras(frase):
    """Recebe uma frase no formato string e retorna o número de palavras
    dela.
    assinatura: string --> int
    testes:
    quant_palavras('Liberdade é a liberdade de dizer que dois mais dois são quatro') == 12
    quant_palavras('Rio de Janeiro') == 3
    quant_palavras('Química') == 1
    """
    return len(str.split(frase))