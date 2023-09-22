def freq_palavras(frases):
    x = {}
    ft = frases.split()
    for r in ft:
        if (r in x):
            x[r] +=1
        else:
            x[r] =1
    return x