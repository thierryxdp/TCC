def freq_palavras(frases):
    d= dict()
    for c in str.split(frases):
        #separa a string em uma lista das diferentes palavras e usa for para passar pela lista
        d[c] = d.get(c, 0) + 1 
        #faz um contador para a frequencia das palavras
    return(d)