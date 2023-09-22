def freq_palavras(frases):
    '''Dado uma string, retorna a quantidade de vezes uma palavra aparece'''
    freq_palavras = {}
    frases = str.strip(frases)
    palavras = str.count (frases, ' ') + 1
    for i in frases:
        freq_palavras = dict.keys(palavras)
        return freq_palavras