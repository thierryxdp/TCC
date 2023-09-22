def freq_palavras(frases):
    frases=str.split(" ")
    
    freq_palavras = [frases.count(p) for p in frases]
    return dict(list(zip(frases,freq_palavras)))