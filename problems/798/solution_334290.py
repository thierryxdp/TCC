def freq_palavras(frases:str)->dict:
    D = {}
    frases = frases.split()
    for i in frases:
        if i in D:
            D[i] += 1
        else:
            D[i] = 1
    return D