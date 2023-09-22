def freq_palavras(frases):
    frases=frases.split()
    final={}
    for i in range(len(frases)):
        b=frases[i]
        final=final+frases.count(b)
    return final