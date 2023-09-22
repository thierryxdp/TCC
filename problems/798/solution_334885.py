def freq_palavras(frases):
    from collections import Counter
    '''Recebe uma string e retorna a quantidade de palavras repetidas dentro dessa string'''
    conta = Counter()
    for palavra in frases:
        conta += [palavra]
    return conta