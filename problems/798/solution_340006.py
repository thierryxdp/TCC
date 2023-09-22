def freq_palavras(frases):
    palavra=list(frases) while str(frases) != " " 
    
    
    freq_palavras = [frases.count(p) for p in frases]
    return dict(list(zip(frases,freq_palavras)))