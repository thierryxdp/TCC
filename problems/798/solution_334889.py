def freq_palavras(frases):
    from collections import Counter
    '''Recebe uma string e retorna a quantidade de palavras repetidas dentro dessa string'''
    freq = {}
    f2 = frases.split
    for i in range(len(frases)):
        palavra = frases[i]
        contar = frases.count(palavra)
        freq[palavra] = contar
    return f2