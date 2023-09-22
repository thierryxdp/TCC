def quant_palavras(frase):
    '''função que calcula o números de palavras
    presentes, numa determinada string
    assinatura:
    casos de teste:'''
    espacos = str.split(frase,)
    return len(espacos)