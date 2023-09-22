def freq_palavras(frases):
    palavras=[]
    for termo in frases:
        if frases[termo] == ' ':
            palavras = palavras + frases[0:termo]
    return palavras