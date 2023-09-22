def freq_palavras(frases):
    frase_sep = str.split(frases)
    
    freq = {}
    
    for palavra in frase_sep:
            
        if palavra in frases:
            quant = str.count(frase_sep,palavra)
            freq[palavra] = quant
    return freq