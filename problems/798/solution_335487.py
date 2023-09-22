def freq_palavras(frases):
    freq={}
    n=0
    separados=frases.split(' ')
    for i in range(len(separados)):
        n=separados.count(separados[i])
        freq[separados[i]]=n
    return freq