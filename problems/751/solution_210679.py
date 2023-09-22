def quant_palavras(frase):
    """Dada uma frase, retorna o número de palavras da frase
    assinatura: str --> int
    testes:
    quant_palavras(batata frita) == 2
    quant_palavras( o dia) == 2
    quant_palavras( retorno do rei ) == 3
    """
    return len(str.split(frase))