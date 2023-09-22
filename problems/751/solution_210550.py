def quant_palavras(frase):
    """Recebe uma frase no formato string e retorna o número de palavras
    dela.
    assinatura: string --> int
    testes:
    quant_palavras('Está muito calor') == 3
    quant_palavras('Manuella Rodrigues') == 2
    quant_palavras('Manu') == 1
    """
    return len(str.split(frase))