def quant_palavras(frase):
    """Recebe uma frase no formato string e retorna o número de palavras
    dela.
    assinatura: string --> int
    testes:
    quant_palavras('Universidade Federal do Rio de Janeiro') == 6
    quant_palavras('Bacharelado em Química') == 3
    quant_palavras('Estela') == 1
    """
    return len(str.split(frase))