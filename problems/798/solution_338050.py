def freq_palavras(frases):
    '''
       Dada uma frase a função retorna um dicionário com as
       palavras da frase como chaves e o valor é a quantidade
       de vezes que a palavra aparece na frase.
       srt -> dict
    '''
    d = dict()
    for palavra in frases:
        if palavra not in d:
            d[palavra] = 1
        else:
            d[palavra] = d + 1
    return d