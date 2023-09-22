def freq_palavras(frases):
    frase=list(frases)
    
    
    freq_palavras = [frases.count(p) for p in frases]
    return dict(list(zip(frases,freq_palavras)))