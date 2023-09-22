def freq_palavras(frases):
    lista = frases.split()
    freq = {} 
    for item in lista: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    return freq