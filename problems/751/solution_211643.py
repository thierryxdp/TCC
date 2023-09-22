def quant_palavras(frase):
    '''função que calcula o números de palavras
    presentes, numa determinada string
    assinatura: str > int
    casos de teste: quant_palavras('oi, tudo bem?') ==3
    quant_palavras('teto sujo, chão sujo') ==4
    quant_palavras('oi') ==1'''
    espacos = str.split(frase,)
    return len(espacos)