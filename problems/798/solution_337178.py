def freq_palavras(frases):
    
    freq = {}
    for pal in frases.split():
        
        if pal not in freq:
            freq[pal] = frases.count(freq)
            

    return freq