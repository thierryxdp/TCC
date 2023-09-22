def freq_palavras(frases):
    'descrição'
    for i in range(frases):
        l_frases = frases.split()
        if i in l_frases:
            return l_frases.count(i)