def freq_palavras(frases:str)->dict:
    D = {}
    freq_palavras = freq_palavras.split()
    for i in freq_palavras:
        if i in D:
            D[i] += 1
        else:
            D[i] = 1
    return D