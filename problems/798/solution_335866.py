def freq_palavras(frases):
    y = frases.split()
    count = Counter(y)
    print (count)