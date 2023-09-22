def freq_palavras(frases):
    low = str.lower(frases)
    frase_sep = str.split(low)
    
    freq = {}
    
    for palavra in frase_sep:
        if palavra in low:
            quant = str.count(low,palavra)
            freq[palavra] = quant
    return freq