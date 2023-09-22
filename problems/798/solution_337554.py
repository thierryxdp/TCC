def freq_palavras(frases):
    '''
    dado uma str como argumento, retorna um dict
    onde as chaves são as palvras da str e os valores
    associados as chaves são a quantidade de vezes
    em que aparecem no texto
    dados de entrada: str
    retorna: dict
    '''
    palavras = str.split(frases)
    freq_palavras = {}
    for i in palavras:
        if i not in freq_palavras:
            freq_palavras[i] = 1
        else:
            freq_palavras[i] = freq_palavras[i] + 1
    return freq_palavras