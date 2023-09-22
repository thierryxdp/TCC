def quant_palavras(frase):
    '''a função recebe uma frase e retorna o numero de palavras da frase
    assinatura: str -> int
    casos de teste:
    quant_palavras('a minha mae adora ler') == 5
    quant_palavras('vou almoçae arroz, feijao e batata frita hoje') == 8
    '''
    palavras = str.split(frase)
    return len(palavras)